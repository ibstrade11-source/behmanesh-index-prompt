from core.rag.claim_selector import (
    select_claims
)

from core.rag.text_splitter import (
    split_into_sentences
)


sample_text = """

Research shows that vaccines
reduce hospitalization risk.

The sky is blue.

Several studies demonstrate
significant effectiveness.

Cats are animals.

Evidence suggests
a measurable benefit.

"""


sentences = split_into_sentences(
    sample_text
)

claims = select_claims(
    sentences,
    max_claims=5
)

for claim in claims:

    print(
        claim.importance_score,
        claim.text
    )
