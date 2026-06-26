"""
RAG-EIG Evidence Summarizer

Experimental v0.1
"""

from core.rag.rag_config import (
    SUPPORT_HIGH,
    CONFLICT_HIGH,
    COVERAGE_HIGH,
    STATUS_SUPPORTED,
    STATUS_CONTRADICTED,
    STATUS_UNDERDETERMINED,
    STATUS_CONTESTED
)


def determine_status(
    support: float,
    conflict: float,
    coverage: float
) -> str:

    if (
        support >= SUPPORT_HIGH
        and conflict < CONFLICT_HIGH
        and coverage >= COVERAGE_HIGH
    ):
        return STATUS_SUPPORTED

    if (
        conflict >= CONFLICT_HIGH
        and coverage >= COVERAGE_HIGH
    ):
        return STATUS_CONTRADICTED

    if (
        coverage < COVERAGE_HIGH
        and support < SUPPORT_HIGH
        and conflict < CONFLICT_HIGH
    ):
        return STATUS_UNDERDETERMINED

    return STATUS_CONTESTED


def summarize_evidence(
    retrieved_items
):

    if not retrieved_items:

        return {
            "external_support": 0.0,
            "external_conflict": 0.0,
            "external_coverage": 0.0,
            "external_status": STATUS_UNDERDETERMINED
        }

    weighted_support = 0.0
    weighted_conflict = 0.0
    trust_sum = 0.0

    for item in retrieved_items:

        weighted_support += (
            item.support_score
            * item.source_trust_score
        )

        weighted_conflict += (
            item.conflict_score
            * item.source_trust_score
        )

        trust_sum += item.source_trust_score

    if trust_sum == 0:

        support = 0.0
        conflict = 0.0

    else:

        support = weighted_support / trust_sum

        conflict = weighted_conflict / trust_sum
    # NOTE: با heuristic backend حداکثر coverage ≈ 0.67
    # coverage واقعی نیازمند vector retrieval در فازهای بعدی است
    # وضعیت "supported" تا آن زمان دست‌نیافتنی است — این محدودیت عمدی است
    coverage = min(
        len(retrieved_items) / 3.0,
        1.0
    )

    status = determine_status(
        support,
        conflict,
        coverage
    )

    return {

        "external_support":
            round(support, 3),

        "external_conflict":
            round(conflict, 3),

        "external_coverage":
            round(coverage, 3),

        "external_status":
            status,

        "retrieved_sources":
            len(retrieved_items)
    }
