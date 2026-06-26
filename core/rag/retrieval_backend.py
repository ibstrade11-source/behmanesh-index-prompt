"""
RAG-EIG Retrieval Backend

Minimal Semantic Retrieval Layer (v0.1)

Goal:
Replace mock retrieval with lightweight
heuristic evidence generation while keeping
future vector DB compatibility.
"""

from dataclasses import dataclass
from typing import List

from core.rag.claim_retriever import RetrievedEvidence
from core.rag.trust_scorer import get_trust_score

# -----------------------------
# Simple Knowledge Heuristics
# -----------------------------

HEURISTIC_KNOWLEDGE = {

    "vaccines": {
        "support": 0.85,
        "conflict": 0.05,
        "source_type": "scientific_database"
    },

    "hospitalization": {
        "support": 0.80,
        "conflict": 0.05,
        "source_type": "scientific_database"
    },

    "moon": {
        "support": 0.10,
        "conflict": 0.80,
        "source_type": "academic_publisher"
    },

    "earth": {
        "support": 0.90,
        "conflict": 0.00,
        "source_type": "scientific_database"
    },

    "boils": {
        "support": 0.95,
        "conflict": 0.00,
        "source_type": "textbook"
    },

    "sun": {
        "support": 0.90,
        "conflict": 0.00,
        "source_type": "scientific_database"
    }
}


def _detect_keywords(text: str) -> List[str]:

    text = text.lower()

    found = []

    for key in HEURISTIC_KNOWLEDGE.keys():

        if key in text:

            found.append(key)

    return found


def retrieve_external_evidence(
    claim: str
):

    """
    Minimal retrieval replacement.

    Produces structured pseudo-evidence
    based on keyword overlap.
    """

    keywords = _detect_keywords(claim)

    evidence: List[RetrievedEvidence] = []

    # If no match → weak generic evidence
    if not keywords:

        evidence.append(
            RetrievedEvidence(
                title="General Knowledge Base",
                source_type="unknown",
                source_trust_score=get_trust_score("unknown"),
                summary="No strong match found in heuristic index.",
                support_score=0.50,
                conflict_score=0.20
            )
        )

        return type("Result", (), {
            "claim": claim,
            "evidence": evidence
        })

    # Build evidence from matched keywords
    for k in keywords:

        meta = HEURISTIC_KNOWLEDGE[k]

        evidence.append(
            RetrievedEvidence(
                title=f"Heuristic Evidence: {k}",
                source_type=meta["source_type"],
                source_trust_score=get_trust_score(meta["source_type"]),
                summary=f"Rule-based match for concept: {k}",
                support_score=meta["support"],
                conflict_score=meta["conflict"]
            )
        )

    return type("Result", (), {
        "claim": claim,
        "evidence": evidence
    })
