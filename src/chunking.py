from typing import List

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50


def chunk_document(content: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    tokens = content.split()
    chunks = []
    step = max(1, chunk_size - overlap)

    for i in range(0, len(tokens), step):
        chunks.append(" ".join(tokens[i:i + chunk_size]))

    return chunks