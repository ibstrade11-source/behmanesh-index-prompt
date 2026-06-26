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


