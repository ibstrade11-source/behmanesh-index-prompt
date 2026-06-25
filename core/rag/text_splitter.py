"""
Text Splitter

Experimental v0.1
"""

from typing import List


def split_into_sentences(
    text: str
) -> List[str]:

    text = text.replace("\n", " ")

    sentences = []

    for chunk in text.split("."):

        chunk = chunk.strip()

        if chunk:

            sentences.append(chunk)

    return sentences
