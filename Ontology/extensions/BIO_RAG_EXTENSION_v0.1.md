BIO_RAG_EXTENSION_v0.1

Status: Experimental Extension

Purpose:

Define ontology elements required for integrating RAG into EIG without modifying CORE BIO ontology.

---

Architectural Principle

RAG is an Evidence Augmentation Layer.

RAG is NOT:

- a reasoning engine
- a scoring engine
- a replacement for CORE
- a replacement for EIG

---

New Concepts

ExternalEvidence

Definition:

Evidence retrieved from sources outside the analyzed document.

Examples:

- scientific papers
- databases
- knowledge bases
- trusted repositories

---

ExternalSupport

Definition:

External evidence supporting a claim.

Relation:

Claim → supported_by → ExternalEvidence

---

ExternalConflict

Definition:

External evidence contradicting a claim.

Relation:

Claim → contradicted_by → ExternalEvidence

---

ExternalCoverage

Definition:

Degree to which a claim area is represented in external knowledge.

Interpretation:

High Coverage:
Large body of relevant evidence exists.

Low Coverage:
Little or no relevant evidence exists.

---

New Relations

Claim
├── supported_by → ExternalEvidence
├── contradicted_by → ExternalEvidence
└── covered_by → ExternalEvidence

---

Epistemic States

Supported

Condition:

High Support
Low Conflict
High Coverage

---

Contradicted

Condition:

Low Support
High Conflict
High Coverage

---

Underdetermined

Condition:

Low Support
Low Conflict
Low Coverage

---

Contested

Condition:

Medium/High Support
Medium/High Conflict
High Coverage

---

Critical Epistemic Rule

No Evidence ≠ Evidence Against

Lack of external evidence shall not be interpreted as contradiction.

This rule protects novel and frontier claims.

---

Integration Scope

This extension affects:

- ExternalEvidence Assessment
- EIG Enhancement Layer

This extension does NOT affect:

- CORE-BEHMANESH
- BIO Core Ontology
- Hybrid Formula
- BSI Score
