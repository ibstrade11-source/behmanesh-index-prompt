RAG_FOR_EIG Specification v0.2

Status: Experimental

Purpose:
External Evidence Retrieval Layer for Epistemic Integrity Gap (EIG)

---

Design Principle

RAG augments evidence assessment.

RAG does not replace:

- CORE-BEHMANESH
- EIG
- BSI Formula
- BIO Ontology

---

External Evidence Variables

external_support_factor

Range:

0.0 → 1.0

Definition:

Degree of support provided by external evidence.

---

external_conflict_factor

Range:

0.0 → 1.0

Definition:

Degree of contradiction provided by external evidence.

---

external_coverage_factor

Range:

0.0 → 1.0

Definition:

Degree of available external evidence coverage.

Interpretation:

0.0 = No evidence available

1.0 = Extensive evidence available

---

External Status

Allowed Values:

- supported
- contradicted
- underdetermined
- contested

---

Status Logic

supported:

support high
conflict low
coverage high

---

contradicted:

support low
conflict high
coverage high

---

underdetermined:

support low
conflict low
coverage low

---

contested:

support medium/high
conflict medium/high
coverage high

---

Critical Principle

No Evidence ≠ Contradicted

Novel claims must not be penalized solely due to lack of external evidence.

---

Experimental Scope

Applies only to EIG.

Does not modify BSI score calculation in Phase 1.
