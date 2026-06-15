from sentence_transformers import SentenceTransformer
import numpy as np


def load_embedding_model(model_name: str = "all-MiniLM-L6-v2", device: str = "cpu"):
    return SentenceTransformer(model_name, device=device)


def encode_chunks(embedding_model, chunk_contents, batch_size: int = 8):
    return embedding_model.encode(
        chunk_contents,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
    )