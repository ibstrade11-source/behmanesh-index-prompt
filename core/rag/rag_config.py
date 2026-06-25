"""
RAG-EIG Experimental Configuration

Phase 1:
Selective Claim-Level Retrieval
"""

# Master Switch

ENABLE_RAG = True

# Retrieval

TOP_K = 5

# Token Budget

MAX_EVIDENCE_TOKENS = 500

# Claim Filtering

MIN_CLAIM_CONFIDENCE = 0.60

# External Evidence Thresholds

SUPPORT_HIGH = 0.70

CONFLICT_HIGH = 0.70

COVERAGE_HIGH = 0.70

# Status Labels

STATUS_SUPPORTED = "supported"

STATUS_CONTRADICTED = "contradicted"

STATUS_UNDERDETERMINED = "underdetermined"

STATUS_CONTESTED = "contested"

# Experimental Flags

ENABLE_EXTERNAL_SUPPORT = True

ENABLE_EXTERNAL_CONFLICT = True

ENABLE_EXTERNAL_COVERAGE = True

# Safety

ALLOW_RAG_TO_MODIFY_BSI_SCORE = False

ALLOW_RAG_TO_MODIFY_CORE = False
