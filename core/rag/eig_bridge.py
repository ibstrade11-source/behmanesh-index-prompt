"""
RAG -> EIG Bridge

Experimental v0.1
"""


def build_eig_signal(
    rag_result: dict
):

    return {

        "external_support":
            rag_result.get(
                "external_support",
                0.0
            ),

        "external_conflict":
            rag_result.get(
                "external_conflict",
                0.0
            ),

        "external_coverage":
            rag_result.get(
                "external_coverage",
                0.0
            ),

        "external_status":
            rag_result.get(
                "external_status",
                "underdetermined"
            )
    }
