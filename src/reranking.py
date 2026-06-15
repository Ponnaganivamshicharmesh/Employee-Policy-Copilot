from typing import List, Tuple


class Document:
    def __init__(self, content, metadata=None):
        self.content = content
        self.metadata = metadata or {}


class Reranker:
    def rerank(self, query: str, documents: List[Tuple[Document, float]], top_k: int = 3) -> List[Tuple[Document, float]]:
        if not documents:
            return []

        q = set(query.lower().split())
        reranked = []

        for doc, orig_score in documents:
            d = set(doc.content.lower().split())
            overlap = len(q & d)
            length_penalty = min(len(doc.content.split()) / 500.0, 1.0)
            score = 0.7 * float(orig_score) + 0.3 * (overlap / (len(q) + 1e-6)) - 0.05 * length_penalty
            reranked.append((doc, score))

        reranked.sort(key=lambda x: x[1], reverse=True)
        return reranked[:top_k]