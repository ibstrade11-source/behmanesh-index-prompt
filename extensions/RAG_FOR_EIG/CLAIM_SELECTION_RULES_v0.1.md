# CLAIM_SELECTION_RULES_v0.1

Purpose:
Determine which claims qualify for external retrieval.

---

Eligible Claims

- Causal claims
- Scientific claims
- Factual assertions
- Quantitative claims
- Comparative claims

---

Non-Eligible Claims

- Definitions
- Pure opinions
- Narrative text
- Procedural text
- Examples

---

Priority Conditions

Run RAG if:

- Internal confidence < threshold
- Weak internal evidence
- High uncertainty
- High preliminary EIG

---

Critical Principle

Not every sentence is a retrieval candidate.

Selective retrieval is mandatory.
