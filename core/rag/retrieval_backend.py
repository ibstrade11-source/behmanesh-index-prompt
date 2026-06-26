"""
RAG-EIG Retrieval Backend

Multi-Source Retrieval Layer (v0.5)

Sources:
1. Wikipedia REST API  (curl-based, general claims)
2. OpenAlex API        (requests-based, academic literature)

Note:
Wikipedia uses subprocess+curl due to SSL handshake
timeout with requests on Termux/Android.
Semantic Scholar excluded: unreachable from this environment.
"""

import json
import subprocess
import requests
from typing import List, Optional
from core.rag.claim_retriever import RetrievedEvidence
from core.rag.trust_scorer import get_trust_score

# --------------------------
# API Config
# --------------------------

WIKIPEDIA_SUMMARY = (
    "https://en.wikipedia.org/api/rest_v1/page/summary/"
)

OPENALEX = (
    "https://api.openalex.org/works"
)

HEADERS_CURL = "User-Agent: BSI-RAG/0.5 (epistemic research)"

HEADERS_REQUESTS = {
    "User-Agent": "BSI-RAG/0.5 (epistemic research)"
}

TIMEOUT = 6


# --------------------------
# Keyword Extractor
# --------------------------

def _extract_keywords(claim: str) -> List[str]:

    stop_words = {
        "the", "a", "an", "is", "are", "was",
        "were", "in", "of", "to", "and", "or",
        "for", "on", "at", "by", "with", "that",
        "this", "it", "as", "be", "has", "have",
        "had", "not", "from", "but", "its", "which",
        "shows", "suggests", "demonstrates", "proves",
        "indicates", "according", "research", "study",
        "evidence", "results", "causes", "because",
        "therefore", "thus", "percent", "higher",
        "lower", "more", "less", "most", "least",
        "reduce", "increase", "improve", "affect", "impact"
    }

    words = (
        claim.lower()
        .replace(",", "")
        .replace(".", "")
        .split()
    )

    keywords = [
        w for w in words
        if w not in stop_words and len(w) > 3
    ]

    return keywords[:3]


# --------------------------
# Conservative Relevance Scorer
# --------------------------

def _score_relevance(
    claim: str,
    extract: str,
    keywords: List[str]
) -> dict:

    extract_lower = extract.lower()

    matched = sum(
        1 for kw in keywords
        if kw in extract_lower
    )

    keyword_coverage = matched / max(len(keywords), 1)

    if keyword_coverage >= 0.5:
        support = round(0.5 + keyword_coverage * 0.3, 3)
    else:
        support = round(keyword_coverage * 0.4, 3)

    conflict = 0.0
    negative_signals = [
        "no evidence",
        "not supported",
        "contradicts",
        "disproven",
        "myth",
        "false claim",
        "debunked"
    ]

    for signal in negative_signals:
        if signal in extract_lower:
            conflict += 0.3

    conflict = min(round(conflict, 3), 1.0)

    return {
        "support": support,
        "conflict": conflict
    }


# --------------------------
# Source 1: Wikipedia (curl)
# --------------------------

def _search_wikipedia(
    query: str,
    keywords: list = []
) -> Optional[dict]:

    try:
        primary = keywords[0] if keywords else query
        url = WIKIPEDIA_SUMMARY + primary.replace(" ", "_")

        cmd = [
            "curl", "-s",
            "--max-time", str(TIMEOUT),
            "-H", HEADERS_CURL,
            url
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return None

        data = json.loads(result.stdout)

        if data.get("type") == "disambiguation":
            return None

        extract = data.get("extract", "")
        title = data.get("title", primary)

        if not extract or len(extract) < 20:
            return None

        return {
            "title": title,
            "extract": extract[:400],
            "source_type": "academic_publisher"
        }

    except Exception:
        return None


# --------------------------
# Source 2: OpenAlex (requests)
# --------------------------

def _decode_inverted_index(inv: dict) -> str:

    if not inv:
        return ""

    words = sorted(
        inv.items(),
        key=lambda x: x[1][0]
    )

    return " ".join(w for w, _ in words[:80])


def _search_openalex(query: str) -> Optional[dict]:

    try:
        r = requests.get(
            OPENALEX,
            params={
                "search": query,
                "per-page": 1,
                "select": "title,abstract_inverted_index"
            },
            headers=HEADERS_REQUESTS,
            timeout=TIMEOUT
        )

        if r.status_code != 200:
            return None

        results = r.json().get("results", [])

        if not results:
            return None

        work = results[0]
        title = work.get("title", query)
        inv = work.get("abstract_inverted_index", {})
        abstract = _decode_inverted_index(inv)

        if not abstract or len(abstract) < 20:
            return None

        return {
            "title": title,
            "extract": abstract[:400],
            "source_type": "peer_reviewed_journal"
        }

    except Exception:
        return None


# --------------------------
# Main Retrieval Function
# --------------------------

def retrieve_external_evidence(claim: str):

    keywords = _extract_keywords(claim)
    query = " ".join(keywords)
    evidence: List[RetrievedEvidence] = []

    sources = [
        ("Wikipedia", lambda q: _search_wikipedia(q, keywords)),
        ("OpenAlex", _search_openalex)
    ]

    for source_name, fetch_fn in sources:

        result = fetch_fn(query)

        if not result:
            continue

        scores = _score_relevance(
            claim,
            result["extract"],
            keywords
        )

        evidence.append(
            RetrievedEvidence(
                title=f"{source_name}: {result['title'][:60]}",
                source_type=result["source_type"],
                source_trust_score=get_trust_score(
                    result["source_type"]
                ),
                summary=result["extract"][:300],
                support_score=scores["support"],
                conflict_score=scores["conflict"]
            )
        )

    if not evidence:
        evidence.append(
            RetrievedEvidence(
                title="No Evidence Found",
                source_type="unknown",
                source_trust_score=get_trust_score("unknown"),
                summary="No relevant source found.",
                support_score=0.0,
                conflict_score=0.0
            )
        )

    return type("Result", (), {
        "claim": claim,
        "evidence": evidence
    })
