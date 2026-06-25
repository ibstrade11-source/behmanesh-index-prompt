"""
RAG-EIG Claim Retriever

Experimental v0.1

Phase 1:
Mock Retrieval Layer
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

    """
    Mock implementation.

    Real retrieval will be added later.
    """

    sample = RetrievedEvidence(

        title="Mock Evidence",

        source_type="scientific_database",

        source_trust_score=0.90,

        summary="Placeholder evidence.",

        support_score=0.50,

        conflict_score=0.00
    )

    return RetrievalResult(

        claim=claim,

        evidence=[sample]
    )
