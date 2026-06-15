from typing import List
from src.retrieval import hybrid_retrieve


class EmployeePolicyCopilot:
    def __init__(
        self,
        chunked_documents: List,
        bm25_index,
        embedding_model,
        query_router,
        reranker=None,
        answer_generator=None,
        query_rewriter=None,
    ):
        self.chunked_documents = chunked_documents
        self.bm25_index = bm25_index
        self.embedding_model = embedding_model
        self.router = query_router
        self.reranker = reranker
        self.answer_generator = answer_generator
        self.query_rewriter = query_rewriter

    def query(
        self,
        user_query: str,
        top_k: int = 5,
        enable_query_rewriting: bool = False,
        enable_reranking: bool = False,
        enable_generation: bool = False,
    ) -> dict:
        pipeline_steps = []

        processed_query = user_query
        if enable_query_rewriting and self.query_rewriter is not None:
            processed_query = self.query_rewriter.rewrite(user_query)
            pipeline_steps.append("Query rewriting: enabled")
        else:
            pipeline_steps.append("Query rewriting: disabled")

        route = self.router.route(processed_query)
        pipeline_steps.append(f"Query router: {route['strategy']} ({route['description']})")

        results = hybrid_retrieve(
            query=processed_query,
            chunked_documents=self.chunked_documents,
            bm25_index=self.bm25_index,
            embedding_model=self.embedding_model,
            top_k=top_k,
            bm25_weight=route.get("bm25_weight", 0.5),
            dense_weight=route.get("dense_weight", 0.5),
        )
        pipeline_steps.append(f"Hybrid retrieval: {len(results)} documents retrieved")

        final_docs = results[:top_k]

        if enable_reranking and self.reranker is not None:
            final_docs = self.reranker.rerank(processed_query, final_docs, top_k=top_k)
            pipeline_steps.append("Reranking: enabled")
        else:
            pipeline_steps.append("Reranking: disabled")

        answer = None
        if enable_generation and self.answer_generator is not None:
            answer = self.answer_generator.generate(processed_query, final_docs)
            pipeline_steps.append("Answer generation: enabled")
        else:
            pipeline_steps.append("Answer generation: disabled")

        return {
            "query": user_query,
            "processed_query": processed_query,
            "retrieved_docs": final_docs,
            "answer": answer,
            "pipeline_steps": pipeline_steps,
        }