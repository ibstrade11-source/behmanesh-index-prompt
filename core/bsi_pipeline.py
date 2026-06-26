"""
BSI Pipeline v3.4.2
SOP: BSI → EIG → ECC → DRAFT → REIG → FINAL SYNTHESIS
"""

from typing import Dict, List
from datetime import datetime
from core.rag.rag_config import ENABLE_RAG
from core.rag.rag_budget import MAX_CLAIMS
from core.rag.text_splitter import split_into_sentences
from core.rag.claim_selector import select_claims
from core.rag.rag_engine import evaluate_claim_with_rag
from core.rag.eig_bridge import build_eig_signal


# ─── STAGE 1: BSI (از bsi_engine موجود) ─────────────────────────────────────

def run_bsi(text: str, engine_result: Dict) -> Dict:
    metrics = engine_result.get("metrics", {})
    layers = engine_result.get("bsi_layers", {})

    return {
        "BSI": round(metrics.get("BSI_score", 0), 1),
        "structure_map": [
            f"domain: {engine_result.get('domain', 'unknown')}",
            f"core_claim: {layers.get('manifest', {}).get('core_claim', '')}",
        ],
        "argument_quality": [
            f"{k}: {v}" for k, v in
            metrics.get("BSI_criteria", {}).items()
        ],
        "evidence_mapping": [
            a.get("assumption", "") for a in
            layers.get("latent", {}).get("assumptions_excavated", [])
        ]
    }


# ─── STAGE 2: EIG ────────────────────────────────────────────────────────────

def run_eig(text: str, bsi_output: Dict, engine_result: Dict) -> Dict:
    layers = engine_result.get("bsi_layers", {})
    eig_data = layers.get("meta", {}).get("EIG", {})
    gaps = eig_data.get("gaps", {})

    # Causal gaps: method-conclusion
    causal_gaps = []
    mcg = gaps.get("method_conclusion", 5)
    if mcg >= 6:
        causal_gaps.append("روش‌شناسی نتیجه‌گیری علّی را پشتیبانی نمی‌کند")
    if mcg >= 4:
        causal_gaps.append("احتمال تعمیم فراتر از داده‌های موجود")

    # Methodological gaps: claim-evidence
    methodological_gaps = []
    ceg = gaps.get("claim_evidence", 5)
    if ceg >= 6:
        methodological_gaps.append("ادعاها فراتر از شواهد ارائه‌شده هستند")
    if ceg >= 4:
        methodological_gaps.append("شواهد ناکافی برای سطح اطمینان ادعاشده")

    # Framing gaps
    framing_gaps = []
    fcg = gaps.get("framing_content", 4)
    if fcg >= 6:
        framing_gaps.append("قاب‌بندی اغراق‌آمیز نسبت به محتوا")

    # Generalization gaps: failure modes
    generalization_gaps = [
        f for f in engine_result.get("failure_modes", [])
        if f != "هیچ failure mode بحرانی شناسایی نشد"
    ]

    # EIG Score: lower gap = higher integrity
    weighted_gap = eig_data.get("weighted_gap", 5)
    eig_score = round((10 - weighted_gap) * 10, 1)

    # ─── RAG Enhancement Layer ───────────────────────────────────────────────
    rag_signals = []
    from core.rag.rag_config import ENABLE_RAG as _RAG_ENABLED
    if _RAG_ENABLED:
        try:
            sentences = split_into_sentences(text)
            top_claims = select_claims(sentences, max_claims=MAX_CLAIMS)
            for c in top_claims:
                if c.importance_score > 0:
                    raw = evaluate_claim_with_rag(c.text)
                    signal = build_eig_signal(raw)
                    signal["claim"] = c.text
                    signal["importance"] = c.importance_score
                    rag_signals.append(signal)
        except Exception:
            rag_signals = []

    return {
        "EIG": eig_score,
        "gaps": {
            "causal_gaps": causal_gaps,
            "methodological_gaps": methodological_gaps,
            "measurement_gaps": framing_gaps,
            "generalization_gaps": generalization_gaps
        },
        "rag_signals": rag_signals,
        "rag_enabled": _RAG_ENABLED
    }


# ─── STAGE 3: ECC ────────────────────────────────────────────────────────────

def run_ecc(bsi_output: Dict, eig_output: Dict) -> Dict:
    bsi = bsi_output["BSI"]
    eig = eig_output["EIG"]

    # Max allowed confidence = min(BSI, EIG) با تعدیل
    max_confidence = round(min(bsi, eig) * 0.9, 1)

    # Overconfidence: BSI خیلی بالاتر از EIG
    overconfidence_flags = []
    if bsi - eig > 15:
        overconfidence_flags.append(
            f"BSI ({bsi}) به طور قابل توجهی بالاتر از EIG ({eig}) است — خطر overclaim"
        )

    all_gaps = (
        eig_output["gaps"]["causal_gaps"] +
        eig_output["gaps"]["methodological_gaps"] +
        eig_output["gaps"]["generalization_gaps"]
    )
    if len(all_gaps) >= 3:
        overconfidence_flags.append(
            f"{len(all_gaps)} شکاف معرفتی شناسایی شده — اطمینان باید محدود شود"
        )

    # Underconfidence: هر دو پایین ولی متن کوتاه
    underconfidence_flags = []
    if bsi < 40 and eig < 40 and len(all_gaps) == 0:
        underconfidence_flags.append(
            "امتیازات پایین ولی شکاف مشخصی یافت نشد — متن ممکن است خیلی کوتاه باشد"
        )

    return {
        "ECC": round((bsi + eig) / 2, 1),
        "confidence_limits": {
            "max_allowed_confidence": max_confidence,
            "overconfidence_flags": overconfidence_flags,
            "underconfidence_flags": underconfidence_flags
        }
    }


# ─── STAGE 4: DRAFT ──────────────────────────────────────────────────────────

def run_draft(bsi_output: Dict, eig_output: Dict, ecc_output: Dict,
              engine_result: Dict) -> Dict:
    layers = engine_result.get("bsi_layers", {})
    core_claim = layers.get("manifest", {}).get("core_claim", "")
    domain = engine_result.get("domain", "unknown")
    assumptions = layers.get("latent", {}).get("assumptions_excavated", [])
    themes = layers.get("latent", {}).get("themes", [])

    bsi = bsi_output["BSI"]
    eig = eig_output["EIG"]
    ecc = ecc_output["ECC"]
    max_conf = ecc_output["confidence_limits"]["max_allowed_confidence"]

    all_gaps = (
        eig_output["gaps"]["causal_gaps"] +
        eig_output["gaps"]["methodological_gaps"] +
        eig_output["gaps"]["measurement_gaps"] +
        eig_output["gaps"]["generalization_gaps"]
    )

    # Draft claims
    draft_claims = []
    if bsi >= 70:
        draft_claims.append("محتوا از کیفیت ساختاری بالایی برخوردار است")
    elif bsi >= 50:
        draft_claims.append("محتوا کیفیت ساختاری متوسطی دارد")
    else:
        draft_claims.append("محتوا نیاز به تقویت ساختاری دارد")

    if eig >= 70:
        draft_claims.append("یکپارچگی معرفتی قابل قبول است")
    else:
        draft_claims.append(f"یکپارچگی معرفتی محدود است — {len(all_gaps)} شکاف شناسایی شد")

    # Interpretation
    if bsi >= 70 and eig >= 70:
        interpretation = f"متن در حوزه {domain} از انسجام معرفتی قابل قبولی برخوردار است."
    elif bsi >= 50 or eig >= 50:
        interpretation = f"متن در حوزه {domain} کیفیت متوسطی دارد و نیاز به تقویت در برخی ابعاد دارد."
    else:
        interpretation = f"متن در حوزه {domain} دارای شکاف‌های معرفتی جدی است که نتیجه‌گیری‌ها را تضعیف می‌کند."

    # Uncertainty acknowledgement
    uncertainty = []
    for gap in all_gaps[:3]:
        uncertainty.append(f"عدم قطعیت: {gap}")
    if assumptions:
        uncertainty.append(
            f"{len(assumptions)} پیش‌فرض ناآزموده وجود دارد که نتایج را مشروط می‌کند"
        )

    return {
        "draft_claims": draft_claims,
        "interpretation": interpretation,
        "provisional_conclusion": (
            f"بر اساس BSI={bsi} و EIG={eig}، "
            f"حداکثر اطمینان مجاز {max_conf} است."
        ),
        "uncertainty_acknowledgement": uncertainty,
        "core_claim_identified": core_claim,
        "themes_detected": [t.get("label", "") for t in themes]
    }


# ─── STAGE 5: REIG ───────────────────────────────────────────────────────────

def run_reig(draft_output: Dict, eig_output: Dict, ecc_output: Dict) -> Dict:
    violations = []
    all_gaps = (
        eig_output["gaps"]["causal_gaps"] +
        eig_output["gaps"]["methodological_gaps"] +
        eig_output["gaps"]["generalization_gaps"]
    )
    max_conf = ecc_output["confidence_limits"]["max_allowed_confidence"]
    overconf = ecc_output["confidence_limits"]["overconfidence_flags"]

    # Check 1: Causal Compliance
    if eig_output["gaps"]["causal_gaps"]:
        if "علیت" not in draft_output["interpretation"] and \
           "شکاف" not in draft_output["interpretation"]:
            violations.append({
                "type": "Causal Compliance",
                "severity": "high",
                "detail": "شکاف علّی در EIG شناسایی شد ولی در Draft منعکس نشد"
            })

    # Check 2: Generalization Compliance
    if eig_output["gaps"]["generalization_gaps"]:
        reflected = any(
            g in str(draft_output["uncertainty_acknowledgement"])
            for g in eig_output["gaps"]["generalization_gaps"]
        )
        if not reflected:
            violations.append({
                "type": "Generalization Compliance",
                "severity": "medium",
                "detail": "تعمیم‌های غیرمجاز در Draft کافی منعکس نشده"
            })

    # Check 3: Overconfidence
    if overconf:
        violations.append({
            "type": "Framing Compliance",
            "severity": "medium",
            "detail": overconf[0]
        })

    # Check 4: Uncertainty coverage
    if len(all_gaps) > 0 and len(draft_output["uncertainty_acknowledgement"]) == 0:
        violations.append({
            "type": "Measurement Compliance",
            "severity": "high",
            "detail": "شکاف‌های معرفتی در بخش uncertainty منعکس نشده‌اند"
        })

    high_count = sum(1 for v in violations if v["severity"] == "high")
    reig_score = max(0, 100 - (high_count * 20) - (len(violations) * 10))
    audit_pass = len(violations) == 0 or (high_count == 0 and len(violations) <= 1)

    return {
        "audit_pass": audit_pass,
        "violations": violations,
        "reig_score": reig_score,
        "correction_required": not audit_pass
    }


# ─── STAGE 6: FINAL SYNTHESIS ────────────────────────────────────────────────

def run_final_synthesis(bsi_output: Dict, eig_output: Dict, ecc_output: Dict,
                        draft_output: Dict, reig_output: Dict) -> Dict:
    bsi = bsi_output["BSI"]
    eig = eig_output["EIG"]
    ecc = ecc_output["ECC"]
    reig = reig_output["reig_score"]

    # Risk state
    avg = (bsi + eig) / 2
    if avg >= 75 and reig >= 80:
        risk_state = "Low"
    elif avg >= 55 and reig >= 60:
        risk_state = "Moderate"
    elif avg >= 35:
        risk_state = "High"
    else:
        risk_state = "Critical"

    # Key limitations
    limitations = draft_output["uncertainty_acknowledgement"][:3]
    if reig_output["violations"]:
        limitations += [v["detail"] for v in reig_output["violations"][:2]]

    # Recommendations
    recommendations = []
    criteria = {}
    for item in bsi_output["argument_quality"]:
        if ": " in item:
            k, v = item.split(": ", 1)
            try:
                criteria[k] = float(v)
            except:
                pass

    weakest = sorted(criteria.items(), key=lambda x: x[1])[:2]
    for k, v in weakest:
        recommendations.append(f"تقویت '{k}' (امتیاز فعلی: {v})")

    if eig_output["gaps"]["causal_gaps"]:
        recommendations.append("تقویت استدلال علّی و کاهش تعمیم‌های ناموجه")
    if eig_output["gaps"]["methodological_gaps"]:
        recommendations.append("افزودن شواهد مستقیم‌تر برای ادعاهای اصلی")

    return {
        "BSI": bsi,
        "EIG": eig,
        "ECC": ecc,
        "REIG": reig,
        "final_interpretation": draft_output["interpretation"],
        "risk_state": risk_state,
        "confidence_profile": {
            "epistemic_confidence": eig,
            "calibration_confidence": ecc_output["confidence_limits"]["max_allowed_confidence"]
        },
        "reig_audit_summary": {
            "status": "PASS" if reig_output["audit_pass"] else "FAIL",
            "key_violations": [v["type"] for v in reig_output["violations"]]
        },
        "core_claim": draft_output["core_claim_identified"],
        "themes": draft_output["themes_detected"],
        "key_limitations": limitations,
        "recommendations": recommendations
    }


# ─── MASTER PIPELINE ─────────────────────────────────────────────────────────

def run_pipeline(text: str, engine_result: Dict) -> Dict:
    """
    BSI Pipeline v3.4.2
    BSI → EIG → ECC → DRAFT → REIG → FINAL SYNTHESIS
    """
    bsi_out = run_bsi(text, engine_result)
    eig_out = run_eig(text, bsi_out, engine_result)
    ecc_out = run_ecc(bsi_out, eig_out)
    draft_out = run_draft(bsi_out, eig_out, ecc_out, engine_result)
    reig_out = run_reig(draft_out, eig_out, ecc_out)
    final_out = run_final_synthesis(bsi_out, eig_out, ecc_out, draft_out, reig_out)

    return {
        "pipeline_version": "3.4.2",
        "timestamp": datetime.utcnow().isoformat(),
        "stages": {
            "bsi": bsi_out,
            "eig": eig_out,
            "ecc": ecc_out,
            "draft": draft_out,
            "reig": reig_out
        },
        "final": final_out
    }
