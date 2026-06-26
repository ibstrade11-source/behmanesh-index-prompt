"""
RAG-EIG Trust Scorer

Experimental v0.1
"""

from dataclasses import dataclass


@dataclass
class SourceTrustScore:
    source_name: str
    trust_score: float
    rationale: str


TRUST_TIERS = {

    "peer_reviewed_journal": 0.95,

    "scientific_database": 0.90,

    "government_source": 0.90,

    "academic_publisher": 0.85,

    "university_repository": 0.80,

    "professional_organization": 0.80,

    "book": 0.75,
    "textbook": 0.80,
    "news_media": 0.60,

    "blog": 0.40,

    "forum": 0.30,

    "social_media": 0.20,

    "unknown": 0.10
}


def get_trust_score(source_type: str) -> float:

    return TRUST_TIERS.get(
        source_type,
        TRUST_TIERS["unknown"]
    )


def build_source_score(
    source_name: str,
    source_type: str
) -> SourceTrustScore:

    score = get_trust_score(source_type)

    return SourceTrustScore(
        source_name=source_name,
        trust_score=score,
        rationale=f"Source classified as {source_type}"
    )
