"""
RAG Pipeline Test Harness
Experimental v0.1

Purpose:
Validate RAG chain in isolation
before pipeline integration.
"""

from core.rag.text_splitter import split_into_sentences
from core.rag.claim_selector import select_claims
from core.rag.rag_engine import evaluate_claim_with_rag


# --------------------------
# Test Cases
# --------------------------

TESTS = [
    {
        "id": "T01",
        "claim": "vaccines reduce hospitalization",
        "expect_status": ["supported", "contested"],
        "expect_support_min": 0.7,
        "expect_conflict_max": 0.3
    },
    {
        "id": "T02",
        "claim": "this novel catalyst improves efficiency by 30 percent",
        "expect_status": ["underdetermined"],
        "expect_coverage_max": 0.5
    },
    {
        "id": "T03",
        "claim": "the moon is made of cheese",
        "expect_status": ["contradicted", "contested"],
        "expect_conflict_min": 0.5
    },
    {
        "id": "T04",
        "claim": "water boils at high temperature",
        "expect_status": ["supported", "contested"],
        "expect_support_min": 0.7
    }
]


# --------------------------
# Claim Selector Tests
# --------------------------

SELECTOR_TEXT = (
    "Research shows vaccines reduce hospitalization. "
    "The sky is blue. "
    "Studies demonstrate significant effectiveness. "
    "Cats are animals. "
    "Because of this, results in higher efficacy."
)

SELECTOR_EXPECTED_TOP = [
    "because",
    "results in",
    "research",
    "shows"
]


# --------------------------
# Runner
# --------------------------

def run_rag_tests():

    passed = 0
    failed = 0

    print("=" * 50)
    print("RAG PIPELINE TEST HARNESS")
    print("=" * 50)
    print()

    for t in TESTS:

        result = evaluate_claim_with_rag(t["claim"])
        status = result.get("external_status")
        support = result.get("external_support", 0)
        conflict = result.get("external_conflict", 0)
        coverage = result.get("external_coverage", 0)

        errors = []

        if status not in t.get("expect_status", [status]):
            errors.append(
                f"status={status} not in {t['expect_status']}"
            )

        if support < t.get("expect_support_min", 0):
            errors.append(
                f"support={support} < {t['expect_support_min']}"
            )

        if conflict > t.get("expect_conflict_max", 1):
            errors.append(
                f"conflict={conflict} > {t['expect_conflict_max']}"
            )

        if coverage > t.get("expect_coverage_max", 1):
            errors.append(
                f"coverage={coverage} > {t['expect_coverage_max']}"
            )

        if conflict < t.get("expect_conflict_min", 0):
            errors.append(
                f"conflict={conflict} < {t['expect_conflict_min']}"
            )

        if errors:
            print(f"[FAIL] {t['id']}: {t['claim'][:40]}")
            for e in errors:
                print(f"       ✗ {e}")
            failed += 1
        else:
            print(f"[PASS] {t['id']}: {t['claim'][:40]}")
            print(f"       status={status} | support={support} | conflict={conflict} | coverage={coverage}")
            passed += 1

    print()

    # Claim Selector Test
    sentences = split_into_sentences(SELECTOR_TEXT)
    claims = select_claims(sentences)
    top_claim = claims[0] if claims else None

    if top_claim and any(
        ind in top_claim.reason
        for ind in SELECTOR_EXPECTED_TOP
    ):
        print("[PASS] T05: claim_selector ranks causal claims highest")
        print(f"       top={top_claim.text[:50]} | score={top_claim.importance_score}")
        passed += 1
    else:
        print("[FAIL] T05: claim_selector did not rank causal claims highest")
        failed += 1

    print()
    print("=" * 50)
    print(f"RESULT: {passed} passed / {failed} failed")
    print("=" * 50)


if __name__ == "__main__":
    run_rag_tests()
