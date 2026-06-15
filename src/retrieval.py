from typing import List, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi


class Document:
    def __init__(self, content, metadata=None):
        self.content = content
        self.metadata = metadata or {}


def build_bm25_index(chunked_documents):
    tokenized = [chunk.content.split() for chunk in chunked_documents]
    return BM25Okapi(tokenized)


def hybrid_retrieve(
    query: str,
    chunked_documents: List[Document],
    bm25_index: BM25Okapi,
    embedding_model,
    top_k: int = 5,
    bm25_weight: float = 0.5,
    dense_weight: float = 0.5
) -> List[Tuple[Document, float]]:
    query_tokens = query.split()
    bm25_scores = bm25_index.get_scores(query_tokens)
    bm25_top_indices = np.argsort(bm25_scores)[-top_k:][::-1]
    bm25_rank = {idx: rank + 1 for rank, idx in enumerate(bm25_top_indices) if bm25_scores[idx] > 0}

    query_embedding = embedding_model.encode(query, convert_to_numpy=True)
    chunk_embeddings = np.array([doc.dense_embedding for doc in chunked_documents])
    dense_similarities = cosine_similarity([query_embedding], chunk_embeddings)[0]
    dense_top_indices = np.argsort(dense_similarities)[-top_k:][::-1]
    dense_rank = {idx: rank + 1 for rank, idx in enumerate(dense_top_indices)}

    rrf_k = 60
    combined_scores = {}

    for idx in set(bm25_rank.keys()) | set(dense_rank.keys()):
        bm25_score = 1 / (rrf_k + bm25_rank[idx]) if idx in bm25_rank else 0
        dense_score = 1 / (rrf_k + dense_rank[idx]) if idx in dense_rank else 0
        combined_scores[idx] = bm25_weight * bm25_score + dense_weight * dense_score

    sorted_indices = sorted(combined_scores.keys(), key=lambda x: combined_scores[x], reverse=True)[:top_k]
    return [(chunked_documents[idx], combined_scores[idx]) for idx in sorted_indices]