RAG_EIG_NOVEL_CLAIM_PROBLEM

Status: Architectural Case Study

Purpose:

Document a critical epistemic failure mode discovered during the design of the RAG-EIG extension.

---

Problem

Initial RAG-EIG design introduced:

- external_support_factor
- external_conflict_factor

However, testing revealed a fundamental issue.

The system could not distinguish:

1. Claims contradicted by external evidence

from

2. Claims for which no external evidence exists

---

Example A

Claim:

"Vaccines cause autism."

External retrieval:

Large amount of evidence available.

Most retrieved evidence contradicts the claim.

Result:

Support = Low

Conflict = High

Coverage = High

Interpretation:

Contradicted

---

Example B

Claim:

"A newly discovered catalyst improves hydrogen efficiency by 30%."

External retrieval:

No relevant evidence found.

Result:

Support = Low

Conflict = Low

Coverage = Low

Interpretation:

Unknown

Not contradicted.

---

Failure Mode

Without an explicit coverage variable:

No Evidence

would be incorrectly treated as:

Evidence Against

This would systematically penalize:

- novel research
- frontier science
- emerging hypotheses

---

Resolution

Introduce:

external_coverage_factor

Range:

0.0 → 1.0

Purpose:

Measure availability of external evidence independently from support or conflict.

---

New Epistemic States

Supported

Contradicted

Underdetermined

Contested

---

Critical Principle

No Evidence ≠ Contradicted

Absence of evidence is not evidence of absence.

Unless external coverage is sufficiently high.

---

Impact on Architecture

Added:

- external_coverage_factor
- underdetermined status

No changes required to:

- CORE-BEHMANESH
- BIO Core Ontology
- Hybrid Formula
- BSI Score

---

Lessons Learned

RAG systems must distinguish:

Lack of evidence

from

Conflicting evidence.

Failure to do so creates an anti-innovation bias in epistemic evaluation systems.
