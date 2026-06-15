import re


class QueryRouter:
    def __init__(self, chunked_documents):
        self.department_keywords = {
            "hr": ["hr", "human resources", "leave", "attendance", "performance"],
            "engineering": ["engineering", "developer", "code", "secure", "technical"],
            "finance": ["finance", "travel", "reimbursement", "expense", "procurement", "meal"],
            "it": ["it", "password", "mfa", "access", "software", "device"],
            "compliance": ["compliance", "privacy", "incident", "data retention", "acceptable use"],
        }

    def classify_query(self, query: str) -> str:
        q = query.lower()
        for department, keywords in self.department_keywords.items():
            if any(keyword in q for keyword in keywords):
                return f"department_{department}"
        if re.search(r"\d+\.\d+", query) or "version" in q:
            return "keyword_heavy"
        return "general"

    def route(self, query: str) -> dict:
        category = self.classify_query(query)

        if category.startswith("department_"):
            dept = category.split("_")[1]
            return {
                "strategy": "filtered_hybrid",
                "filters": {"department": dept},
                "bm25_weight": 0.5,
                "dense_weight": 0.5,
                "description": f"Filtering for {dept} department policies",
            }

        if category == "keyword_heavy":
            return {
                "strategy": "bm25_heavy",
                "filters": {},
                "bm25_weight": 0.8,
                "dense_weight": 0.2,
                "description": "BM25-heavy retrieval for keyword-specific queries",
            }

        return {
            "strategy": "full_hybrid",
            "filters": {},
            "bm25_weight": 0.5,
            "dense_weight": 0.5,
            "description": "Full hybrid retrieval",
        }