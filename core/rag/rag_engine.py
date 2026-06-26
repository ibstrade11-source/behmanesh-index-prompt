"""
RAG-EIG Engine

Experimental v0.1

End-to-End Pipeline (Clean Wiring Version)
"""
from core.rag.evidence_summarizer import (
    summarize_evidence
)

from core.rag.rag_config import (
    ENABLE_RAG
)

from core.rag.retrieval_backend import (
    retrieve_external_evidence
)

from core.rag.eig_bridge import (
    build_eig_signal)

def evaluate_claim_with_rag(
    claim: str
):

    """
    End-to-end RAG-EIG evaluation pipeline.

    Steps:
    1. Retrieve evidence (backend)
    2. Summarize evidence
    3. Return structured epistemic signal
    """

    # --------------------------
    # Safety / Toggle Layer
    # --------------------------
    if not ENABLE_RAG:

        return {
            "enabled": False
        }

    # --------------------------
    # Retrieval Phase
    # --------------------------
    retrieval_result = retrieve_external_evidence(claim)

    # --------------------------
    # Evidence Aggregation
    # --------------------------
    summary = summarize_evidence(
        retrieval_result.evidence
    )

   # --------------------------
    # Final Output (EIG-ready)
    # --------------------------
    eig_signal = build_eig_signal(summary)

    return {

        "enabled": True,

        "claim": claim,

        **eig_signal,

        "retrieved_sources": summary.get("retrieved_sources", 0)
    }
