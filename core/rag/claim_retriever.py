"""
RAG-EIG Claim Retriever

Experimental v0.2

Phase 1.5:
Deterministic Heuristic Retrieval
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

evidence = []

if (
    "vaccine" in text
    or "vaccines" in text
):

    evidence.append(
        RetrievedEvidence(
            title="Scientific Consensus",
            source_type="scientific_database",
            source_trust_score=0.90,
            summary="Evidence generally supports vaccine effectiveness.",
            support_score=0.85,
            conflict_score=0.05
        )
    )

elif (
    "moon" in text
    and "cheese" in text
):

    evidence.append(
        RetrievedEvidence(
            title="Astronomy Reference",
            source_type="academic_publisher",
            source_trust_score=0.85,
            summary="Claim conflicts with established astronomy.",
            support_score=0.05,
            conflict_score=0.95
        )
    )

elif (
    "earth" in text
    and "two suns" in text
):

    evidence.append(
        RetrievedEvidence(
            title="Astronomy Reference",
            source_type="scientific_database",
            source_trust_score=0.90,
            summary="Earth has one sun.",
            support_score=0.05,
            conflict_score=0.95
        )
    )

elif (
    "water boils" in text
):

    evidence.append(
        RetrievedEvidence(
            title="Physics Reference",
            source_type="academic_publisher",
            source_trust_score=0.85,
            summary="Consistent with standard atmospheric pressure.",
            support_score=0.95,
            conflict_score=0.00
        )
    )

else:

    evidence.append(
        RetrievedEvidence(
            title="Unknown Evidence",
            source_type="unknown",
            source_trust_score=0.10,
            summary="Insufficient external evidence.",
            support_score=0.50,
            conflict_score=0.00
        )
    )

return RetrievalResult(
    claim=claim,
    evidence=evidence
)
