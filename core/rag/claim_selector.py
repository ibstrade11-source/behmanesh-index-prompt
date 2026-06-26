"""
Claim Selector

Experimental v0.1

Purpose:
Select epistemically important claims
before RAG retrieval.
"""

from dataclasses import dataclass
from typing import List
from core.rag.rag_budget import MAX_CLAIMS


@dataclass
class ClaimCandidate:

    text: str

    importance_score: float

    reason: str

def score_claim(
    sentence: str
) -> ClaimCandidate:

    score = 0.0

    lowered = sentence.lower()

    causal_indicators = [
        "therefore",
        "thus",
        "because",
        "causes",
        "results in",
        "proves"
    ]

    evidence_indicators = [
        "evidence",
        "research",
        "study",
        "shows",
        "demonstrates",
        "demonstrate",
        "indicates",
        "suggests",
        "according to"
    ]

    matched = []

    for indicator in causal_indicators:
        if indicator in lowered:
            score += 2.0
            matched.append(indicator)

    for indicator in evidence_indicators:
        if indicator in lowered:
            score += 1.0
            matched.append(indicator)

    if any(char.isdigit() for char in sentence):
        score += 0.5

    return ClaimCandidate(
        text=sentence,
        importance_score=round(score, 2),
        reason=", ".join(matched)
    )

def select_claims(
    sentences: List[str],
    max_claims: int = MAX_CLAIMS
) -> List[ClaimCandidate]:

    scored = [

        score_claim(sentence)

        for sentence in sentences
    ]

    scored.sort(

        key=lambda x: x.importance_score,

        reverse=True
    )

    return scored[:max_claims]
