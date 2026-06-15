from typing import List


def evaluate_rag(copilot, evaluation_qa: List[dict], top_k: int = 3, enable_query_rewriting: bool = False) -> dict:
    results = []

    for qa in evaluation_qa:
        query = qa["query"]
        expected_docs = qa.get("retrieval_gt_doc_ids", [])

        result = copilot.query(
            user_query=query,
            top_k=top_k,
            enable_query_rewriting=enable_query_rewriting,
            enable_reranking=False,
            enable_generation=False,
        )

        retrieved_pairs = []
        for doc, _ in result["retrieved_docs"]:
            folder = doc.metadata.get("folder", "")
            file_name = doc.metadata.get("file_name", "").replace(".txt", "")
            retrieved_pairs.append(f"{folder}/{file_name}")

        retrieval_hit = int(any(expected in retrieved_pairs for expected in expected_docs))

        results.append(
            {
                "query": query,
                "processed_query": result["processed_query"],
                "retrieved_pairs": retrieved_pairs,
                "expected_docs": expected_docs,
                "retrieval_hit": retrieval_hit,
            }
        )

    total_queries = len(results)
    retrieval_hits = sum(r["retrieval_hit"] for r in results)
    retrieval_accuracy = retrieval_hits / total_queries if total_queries else 0

    return {
        "total_queries": total_queries,
        "retrieval_hits": retrieval_hits,
        "retrieval_accuracy": retrieval_accuracy,
        "individual_results": results,
    }