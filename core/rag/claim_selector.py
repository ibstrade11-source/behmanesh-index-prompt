"""
Claim Selector

Experimental v0.1

Purpose:
Select epistemically important claims
before RAG retrieval.
"""

from dataclasses import dataclass
from typing import List


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

    indicators = [

        "therefore",
        "thus",
        "because",
        "evidence",
        "research",
        "study",
        "shows",
        "demonstrates",
        "causes",
        "results in",
        "proves",
        "indicates",
        "suggests",
        "according to"

    ]

    matched = []

    for indicator in indicators:

        if indicator in lowered:

            score += 1.0
            matched.append(indicator)

    score += min(
        len(sentence) / 200,
        1.0
    )

    return ClaimCandidate(

        text=sentence,

        importance_score=round(score, 2),

        reason=", ".join(matched)
    )


def select_claims(
    sentences: List[str],
    max_claims: int = 10
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
