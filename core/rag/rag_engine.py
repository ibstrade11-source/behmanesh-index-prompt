"""
RAG-EIG Engine

Experimental v0.1

End-to-End Pipeline
"""

from core.rag.claim_retriever import (
    retrieve_external_evidence
)

from core.rag.evidence_summarizer import (
    summarize_evidence
)

from core.rag.rag_config import (
    ENABLE_RAG
)


def evaluate_claim_with_rag(
    claim: str
):

    if not ENABLE_RAG:

        return {
            "enabled": False
        }

    retrieval_result = (
        retrieve_external_evidence(claim)
    )

    summary = summarize_evidence(
        retrieval_result.evidence
    )

    return {

        "enabled": True,

        "claim": claim,

        **summary
    }
