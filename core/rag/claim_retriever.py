"""
RAG-EIG Claim Retriever

Experimental v0.2

Phase 1.5:
Heuristic Retrieval Layer
"""

from dataclasses import dataclass
from typing import List

@dataclass
class RetrievedEvidence:

title: str

source_type: str

source_trust_score: float

summary: str

support_score: float

conflict_score: float

@dataclass
class RetrievalResult:

claim: str

evidence: List[RetrievedEvidence]

def retrieve_external_evidence(
claim: str
) -> RetrievalResult:

text = claim.lower()

if "vaccine" in text or "vaccines" in text:

    evidence = [
        RetrievedEvidence(
            title="Scientific Evidence",
            source_type="scientific_database",
            source_trust_score=0.90,
            summary="Evidence supports effectiveness.",
            support_score=0.85,
            conflict_score=0.05
        )
    ]

elif (
    "moon" in text
    and "cheese" in text
):

    evidence = [
        RetrievedEvidence(
            title="Astronomy Evidence",
            source_type="academic_publisher",
            source_trust_score=0.85,
            summary="Claim conflicts with established astronomy.",
            support_score=0.05,
            conflict_score=0.95
        )
    ]

elif (
    "earth" in text
    and "two suns" in text
):

    evidence = [
        RetrievedEvidence(
            title="Astronomy Evidence",
            source_type="scientific_database",
            source_trust_score=0.90,
            summary="Earth has one sun.",
            support_score=0.05,
            conflict_score=0.95
        )
    ]

elif (
    "water boils"
    in text
):

    evidence = [
        RetrievedEvidence(
            title="Physics Reference",
            source_type="academic_publisher",
            source_trust_score=0.85,
            summary="Consistent with standard conditions.",
            support_score=0.95,
            conflict_score=0.00
        )
    ]

else:

    evidence = [
        RetrievedEvidence(
            title="Unknown Evidence",
            source_type="unknown",
            source_trust_score=0.10,
            summary="Insufficient external evidence.",
            support_score=0.50,
            conflict_score=0.00
        )
    ]

return RetrievalResult(
    claim=claim,
    evidence=evidence
)
