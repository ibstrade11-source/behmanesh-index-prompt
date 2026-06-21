"""
BSI Engine v3.4.1 — Real Implementation
Based on SOP_Intellectual_Content_Analysis_v3.4.1
"""

import re
from typing import Dict, List, Tuple


# ─── Claim Classification ───────────────────────────────────────────────────

FACT_MARKERS = [
    "نشان داده شده", "اثبات شده", "مستند است", "طبق داده‌ها",
    "studies show", "proven", "data indicates", "research confirms",
    "measured", "documented", "observed", "statistically significant"
]
INFERENCE_MARKERS = [
    "به نظر می‌رسد", "احتمالاً", "ممکن است", "شواهد نشان می‌دهد",
    "suggests", "likely", "appears", "may", "could", "implies",
    "indicates", "seems"
]
HYPOTHESIS_MARKERS = [
    "فرض می‌کنیم", "اگر درست باشد", "تئوری این است",
    "hypothetically", "if true", "theory suggests", "we propose",
    "assuming", "in theory"
]
SPECULATION_MARKERS = [
    "ممکن است روزی", "شاید", "تصور می‌کنم",
    "perhaps", "might someday", "I imagine", "speculative",
    "conceivably", "could potentially"
]


def classify_claim(sentence: str) -> str:
    s = sentence.lower()
    for m in FACT_MARKERS:
        if m in s:
            return "FACT"
    for m in INFERENCE_MARKERS:
        if m in s:
            return "INFERENCE"
    for m in HYPOTHESIS_MARKERS:
        if m in s:
            return "HYPOTHESIS"
    for m in SPECULATION_MARKERS:
        if m in s:
            return "SPECULATION"
    return "INFERENCE"  # default per BSI protocol


# ─── Core Claim Extraction (گام ۰) ─────────────────────────────────────────

def extract_core_claim(text: str) -> str:
    sentences = [s.strip() for s in re.split(r'[.!?؟।\n]', text) if len(s.strip()) > 20]
    if not sentences:
        return "متن فاقد ادعای مرکزی مشخص است — محتوا پراکنده یا صرفاً توصیفی است."

    # Priority: first sentence with a strong verb claim
    claim_indicators = [
        "argue", "claim", "show", "prove", "demonstrate", "propose",
        "این مقاله", "ادعا می‌کند", "نشان می‌دهد", "پیشنهاد می‌کند",
        "we find", "we show", "results indicate", "study shows",
        "this paper", "we propose", "we demonstrate"
    ]
    for sent in sentences[:5]:
        for ind in claim_indicators:
            if ind in sent.lower():
                return sent

    # Fallback: longest sentence in first 3
    return max(sentences[:3], key=len) if sentences else "Core Claim قابل استخراج نیست."


# ─── Domain Detection (گام ۱) ───────────────────────────────────────────────

DOMAIN_KEYWORDS = {
    "physics_mathematics": ["theorem", "proof", "equation", "quantum", "calculus",
                            "topology", "matrix", "eigenvalue", "differential"],
    "biomedical": ["clinical", "patient", "drug", "trial", "diagnosis", "gene",
                   "protein", "RCT", "placebo", "epidemiology", "cancer"],
    "economics_behavioral": ["market", "GDP", "utility", "behavioral", "Nash",
                              "elasticity", "regression", "endogeneity", "causal"],
    "computer_science_ai": ["algorithm", "neural", "training", "dataset", "model",
                             "accuracy", "benchmark", "deep learning", "transformer"],
    "general_scientific": ["hypothesis", "methodology", "experiment", "sample",
                            "statistical", "p-value", "correlation", "variable"]
}


def detect_domain(text: str) -> str:
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in text_lower)
    top = max(scores, key=scores.get)
    return top if scores[top] > 0 else "general"


# ─── EIG Scoring (گام ۳ — Meta Layer) ──────────────────────────────────────

def score_method_conclusion_gap(text: str, sentences: List[str]) -> float:
    """
    Method-Conclusion Gap (وزن ۳۰٪)
    آیا روش‌شناسی واقعاً نتیجه‌گیری را پشتیبانی می‌کند؟
    """
    gap = 5.0  # baseline

    # Penalty: generalizing from specific
    generalize = ["in general", "always", "universally", "همیشه", "به طور کلی",
                  "all cases", "every", "never", "proves that", "اثبات می‌کند که"]
    specific_method = ["sample of", "in this study", "limited to", "only in",
                       "نمونه", "محدود به", "در این مطالعه"]

    has_generalization = any(g in text.lower() for g in generalize)
    has_limited_method = any(s in text.lower() for s in specific_method)

    if has_generalization and has_limited_method:
        gap += 3.0  # high gap: limited method → broad conclusion
    elif has_generalization:
        gap += 1.5
    elif has_limited_method:
        gap -= 1.0  # honest about limitations → lower gap

    # Correlation vs causation
    if any(w in text.lower() for w in ["correlation", "همبستگی", "associated with"]):
        if any(w in text.lower() for w in ["cause", "effect", "علت", "باعث"]):
            gap += 2.0

    return min(10.0, max(0.0, gap))


def score_claim_evidence_gap(text: str, sentences: List[str]) -> float:
    """
    Claim-Evidence Gap (وزن ۳۵٪)
    آیا شواهد ارائه‌شده ادعاها را پشتیبانی می‌کنند؟
    """
    gap = 5.0

    # Positive signals (evidence present)
    evidence_markers = ["according to", "data shows", "figure", "table",
                        "p-value", "confidence interval", "n=", "cited",
                        "طبق", "داده‌ها نشان", "جدول", "شکل", "منبع"]
    evidence_count = sum(1 for m in evidence_markers if m in text.lower())

    # Negative signals (claims without evidence)
    bare_claims = ["it is clear that", "obviously", "everyone knows",
                   "undoubtedly", "واضح است", "بدیهی است", "مشخص است"]
    bare_count = sum(1 for m in bare_claims if m in text.lower())

    gap -= min(3.0, evidence_count * 0.5)
    gap += min(3.0, bare_count * 1.5)

    return min(10.0, max(0.0, gap))


def score_framing_content_gap(text: str) -> float:
    """
    Framing-Content Gap (وزن ۱۵٪)
    آیا قاب‌بندی همان چیزی را می‌گوید که محتوا نشان می‌دهد؟
    """
    gap = 4.0

    # Strong framing words that may not match content
    strong_framing = ["revolutionary", "breakthrough", "unprecedented", "novel",
                      "انقلابی", "بی‌سابقه", "کاملاً جدید", "first ever",
                      "game-changing", "transformative"]
    hedging = ["suggests", "may", "could", "limited", "preliminary",
               "ممکن است", "احتمالاً", "محدود", "اولیه"]

    framing_count = sum(1 for w in strong_framing if w in text.lower())
    hedging_count = sum(1 for w in hedging if w in text.lower())

    if framing_count > 2 and hedging_count > 3:
        gap += 2.5  # strong claims but heavily hedged content
    elif framing_count > 1:
        gap += 1.0

    return min(10.0, max(0.0, gap))


def score_longitudinal_gap() -> Tuple[float, str]:
    """
    Longitudinal Consistency Gap (وزن ۲۰٪)
    بدون داده تاریخی → نامشخص، تعدیل ۲۵٪
    """
    raw_score = 5.0
    adjusted = raw_score * 0.75  # BSI protocol: unknown → 25% discount
    return adjusted, "INFERENCE — اطمینان پایین (داده تاریخی موجود نیست)"


def compute_eig_score(mcg: float, ceg: float, fcg: float, lcg: float) -> Dict:
    """
    EIG Score نهایی با وزن‌های رسمی BSI v3.4.1
    """
    weighted = (mcg * 0.30) + (ceg * 0.35) + (fcg * 0.15) + (lcg * 0.20)
    # Convert gap score to integrity score (lower gap = higher integrity)
    integrity_score = round((10 - weighted) * 10, 1)

    if integrity_score >= 80:
        classification = "HIGH_INTEGRITY"
    elif integrity_score >= 60:
        classification = "MODERATE_INTEGRITY"
    elif integrity_score >= 40:
        classification = "LOW_INTEGRITY"
    else:
        classification = "CRITICAL_GAPS"

    return {
        "gaps": {
            "method_conclusion": round(mcg, 2),
            "claim_evidence": round(ceg, 2),
            "framing_content": round(fcg, 2),
            "longitudinal_consistency": round(lcg, 2)
        },
        "weighted_gap": round(weighted, 2),
        "EIG_score": integrity_score,
        "classification": classification
    }


# ─── BSI Scoring (گام ۵) ────────────────────────────────────────────────────

BSI_WEIGHTS = {
    "conditional_depth": 0.22,       # عمق شرطی و پیش‌بینی‌کننده
    "referential_continuity": 0.18,  # تداوم ارجاعی
    "ethical_layer": 0.18,           # لایه اخلاقی
    "creativity_value": 0.17,        # خلاقیت و ارزش افزوده
    "depth_over_breadth": 0.12,      # کمتر اما عمیق‌تر
    "cross_domain": 0.08,            # گستردگی چندحوزه‌ای
    "anti_drift": 0.05               # اجتناب از performative drift
}


def score_bsi_criteria(text: str, domain: str, eig: Dict) -> Dict:
    text_lower = text.lower()
    sentences = [s.strip() for s in re.split(r'[.!?؟\n]', text) if len(s.strip()) > 15]
    word_count = len(text.split())

    # Conditional depth: "if...then", شرطی‌بندی
    conditional = sum(1 for s in sentences if any(
        w in s.lower() for w in ["if", "اگر", "when", "given that", "assuming", "provided"]
    ))
    conditional_score = min(100, 40 + conditional * 15)

    # Referential continuity: citations, references
    ref_markers = ["et al", "ibid", "op.cit", "منبع", "ارجاع", "مطالعه قبلی",
                   "previously", "as shown in", "building on"]
    ref_count = sum(1 for m in ref_markers if m in text_lower)
    continuity_score = min(100, 50 + ref_count * 10)

    # Ethical layer: acknowledgment of limitations, bias
    ethical_markers = ["limitation", "bias", "conflict of interest", "محدودیت",
                       "تعارض منافع", "سوگیری", "acknowledge", "caveat"]
    ethical_count = sum(1 for m in ethical_markers if m in text_lower)
    ethical_score = min(100, 45 + ethical_count * 15)

    # Creativity / value-add: novel framing, metaphor
    creative_markers = ["novel", "unlike", "in contrast", "reframe", "جدید",
                        "برخلاف", "متفاوت از", "propose", "پیشنهاد می‌کنیم"]
    creative_count = sum(1 for m in creative_markers if m in text_lower)
    creativity_score = min(100, 50 + creative_count * 10)

    # Depth over breadth: long focused sentences
    avg_sent_len = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
    depth_score = min(100, 40 + avg_sent_len * 2)

    # Cross-domain: mentions of different fields
    domains_mentioned = sum(1 for d, kws in DOMAIN_KEYWORDS.items()
                            if d != domain and any(kw in text_lower for kw in kws))
    cross_score = min(100, 40 + domains_mentioned * 20)

    # Anti-drift: avoids repetition and vague claims
    vague = ["it is important", "very significant", "مهم است", "بسیار مهم",
             "clearly", "obviously", "as everyone knows"]
    vague_count = sum(1 for v in vague if v in text_lower)
    drift_score = max(0, min(100, 80 - vague_count * 15))

    scores = {
        "conditional_depth": conditional_score,
        "referential_continuity": continuity_score,
        "ethical_layer": ethical_score,
        "creativity_value": creativity_score,
        "depth_over_breadth": depth_score,
        "cross_domain": cross_score,
        "anti_drift": drift_score
    }

    bsi_total = sum(scores[k] * BSI_WEIGHTS[k] for k in BSI_WEIGHTS)
    return {"criteria_scores": scores, "bsi_score": round(bsi_total, 1)}


# ─── Assumption Excavation (لایه Latent) ────────────────────────────────────

def excavate_assumptions(text: str) -> List[Dict]:
    assumptions = []

    checks = [
        {
            "type": "methodological",
            "label": "روش‌شناختی",
            "trigger": ["sample", "نمونه", "survey", "experiment", "data collection"],
            "assumption": "نمونه انتخاب‌شده نماینده جمعیت هدف است",
            "rank": "foundational"
        },
        {
            "type": "modeling",
            "label": "مدل‌سازی",
            "trigger": ["model", "مدل", "equation", "parameter", "variable"],
            "assumption": "متغیرهای انتخاب‌شده تمام عوامل مؤثر را پوشش می‌دهند",
            "rank": "foundational"
        },
        {
            "type": "generalizability",
            "label": "تعمیم‌پذیری",
            "trigger": ["conclude", "نتیجه", "therefore", "thus", "hence", "بنابراین"],
            "assumption": "یافته‌ها به سایر زمینه‌ها قابل تعمیم هستند",
            "rank": "supporting"
        },
        {
            "type": "normative",
            "label": "ارزشی",
            "trigger": ["should", "must", "باید", "ought", "recommend", "توصیه"],
            "assumption": "ارزش‌های پیش‌فرض نویسنده با ارزش‌های مخاطب یکسان است",
            "rank": "secondary"
        }
    ]

    text_lower = text.lower()
    for check in checks:
        if any(trigger in text_lower for trigger in check["trigger"]):
            assumptions.append({
                "type": check["type"],
                "label": check["label"],
                "assumption": check["assumption"],
                "rank": check["rank"],
                "violation_test": f"اگر این پیش‌فرض غلط باشد: نتیجه‌گیری اصلی بی‌اعتبار می‌شود"
                    if check["rank"] == "foundational"
                    else "اگر این پیش‌فرض غلط باشد: نتیجه تضعیف می‌شود اما کاملاً رد نمی‌شود"
            })

    return assumptions


# ─── Theme Detection (گام ۴) ────────────────────────────────────────────────

def detect_themes(text: str) -> List[Dict]:
    themes = []
    text_lower = text.lower()

    theme_map = [
        ("epistemology", ["knowledge", "evidence", "truth", "معرفت", "شواهد", "حقیقت"],
         "معرفت‌شناختی"),
        ("methodology", ["method", "approach", "process", "روش", "رویکرد", "فرآیند"],
         "روش‌شناختی"),
        ("ethics", ["ethical", "moral", "value", "اخلاق", "ارزش", "عدالت"],
         "اخلاقی"),
        ("innovation", ["new", "novel", "innovative", "جدید", "نوآوری", "خلاقانه"],
         "نوآوری"),
        ("critique", ["problem", "limitation", "gap", "مشکل", "محدودیت", "شکاف"],
         "انتقادی"),
    ]

    for key, keywords, label in theme_map:
        count = sum(1 for kw in keywords if kw in text_lower)
        if count >= 2:
            themes.append({
                "theme": key,
                "label": label,
                "frequency": count,
                "type": "DominantTheme" if count >= 4 else "SecondaryTheme"
            })

    return themes[:4]  # top 4 themes


# ─── Failure Modes ──────────────────────────────────────────────────────────

def detect_failure_modes(eig: Dict, domain: str, assumptions: List) -> List[str]:
    modes = []
    gaps = eig["gaps"]

    if gaps["method_conclusion"] >= 6:
        modes.append("Method-Conclusion Gap بحرانی: روش‌شناسی نتیجه‌گیری را پشتیبانی نمی‌کند")
    if gaps["claim_evidence"] >= 6:
        modes.append("Claim-Evidence Gap بالا: ادعاها فراتر از شواهد ارائه‌شده هستند")
    if gaps["framing_content"] >= 6:
        modes.append("Framing-Content Gap: قاب‌بندی اغراق‌آمیز نسبت به محتوا")

    foundational = [a for a in assumptions if a["rank"] == "foundational"]
    if len(foundational) >= 2:
        modes.append(f"{len(foundational)} پیش‌فرض بنیادین ناآزموده وجود دارد")

    if domain == "computer_science_ai":
        modes.append("خطر: فقدان ablation study یا benchmark مستقل")
    elif domain == "economics_behavioral":
        modes.append("خطر: مشکل احتمالی endogeneity در مدل علّی")
    elif domain == "biomedical":
        modes.append("خطر: نیاز به ارزیابی GRADE و تأیید external validity")

    return modes if modes else ["هیچ failure mode بحرانی شناسایی نشد"]


# ─── Main Engine ─────────────────────────────────────────────────────────────

class BSIEngine:

    def analyze_document(self, document: Dict) -> Dict:
        text = document.get("text", "") or document.get("content", "")
        title = document.get("title", "Untitled")
        doc_id = document.get("id", "unknown")

        if not text:
            return {"error": "متن ورودی خالی است", "document_id": doc_id}

        sentences = [s.strip() for s in re.split(r'[.!?؟\n]', text) if len(s.strip()) > 15]

        # گام ۰: Core Claim
        core_claim = extract_core_claim(text)

        # گام ۱: Domain
        domain = document.get("domain") or detect_domain(text)

        # گام ۳: EIG
        mcg = score_method_conclusion_gap(text, sentences)
        ceg = score_claim_evidence_gap(text, sentences)
        fcg = score_framing_content_gap(text)
        lcg_score, lcg_note = score_longitudinal_gap()
        eig = compute_eig_score(mcg, ceg, fcg, lcg_score)

        # Assumption Excavation
        assumptions = excavate_assumptions(text)

        # گام ۴: Themes
        themes = detect_themes(text)

        # گام ۵: BSI Score
        bsi_result = score_bsi_criteria(text, domain, eig)

        # Failure Modes
        failure_modes = detect_failure_modes(eig, domain, assumptions)

        # Claim classification sample
        claim_labels = [
            {"sentence": s[:100], "label": classify_claim(s)}
            for s in sentences[:5]
        ]

        return {
            "document_id": doc_id,
            "title": title,
            "domain": domain,
            "bsi_layers": {
                "manifest": {
                    "core_claim": core_claim,
                    "claim_classifications": claim_labels
                },
                "latent": {
                    "assumptions_excavated": assumptions,
                    "themes": themes
                },
                "meta": {
                    "EIG": eig,
                    "longitudinal_note": lcg_note
                }
            },
            "metrics": {
                "EIG_score": eig["EIG_score"],
                "EIG_classification": eig["classification"],
                "BSI_score": bsi_result["bsi_score"],
                "BSI_criteria": bsi_result["criteria_scores"]
            },
            "failure_modes": failure_modes
        }

    def run_batch(self, request: Dict) -> Dict:
        results = []
        for doc in request.get("documents", []):
            results.append(self.analyze_document(doc))

        bsi_scores = [r["metrics"]["BSI_score"] for r in results if "metrics" in r]
        eig_scores = [r["metrics"]["EIG_score"] for r in results if "metrics" in r]

        return {
            "summary": {
                "total_documents": len(results),
                "global_bsi_score": round(sum(bsi_scores) / len(bsi_scores), 1) if bsi_scores else 0,
                "global_eig_score": round(sum(eig_scores) / len(eig_scores), 1) if eig_scores else 0
            },
            "results": results,
            "meta": {"bsi_version": "3.4.1"}
        }


def compute_bsi(text: str) -> dict:
    engine = BSIEngine()
    doc = {"id": "auto", "title": "auto", "text": text}
    result = engine.analyze_document(doc)
    bsi = result["metrics"]["BSI_score"] / 100
    eig = result["metrics"]["EIG_score"] / 100
    if bsi >= 0.75:
        label = "HIGH_INTEGRITY"
    elif bsi >= 0.55:
        label = "MODERATE_INTEGRITY"
    elif bsi >= 0.35:
        label = "LOW_INTEGRITY"
    else:
        label = "CRITICAL_GAPS"
    return {"bsi": round(bsi, 4), "eig": round(eig, 4), "label": label, "details": result}
