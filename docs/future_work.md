# Future Work

## Planned Improvements

### 1. Better Chunking
The current chunking strategy uses fixed-size overlapping windows. Future work could use sentence-aware or structure-aware chunking to preserve policy sections more cleanly.

### 2. Stronger Reranking
The current reranker is a lightweight heuristic. A cross-encoder reranker or a learned reranking model could improve top-k quality.

### 3. Better Query Routing
The current router uses keyword rules. A trained intent classifier could provide more accurate routing decisions.

### 4. Out-of-Scope Detection
The system should detect unsupported questions and respond with a refusal or fallback message instead of trying to retrieve irrelevant documents.

### 5. Azure-Native Version
A future version could replace local retrieval components with Azure AI Search and use Azure OpenAI or another managed generation service.

### 6. Web UI
A simple Streamlit or FastAPI interface would make the copilot easier to demonstrate in a portfolio or interview setting.

### 7. More Evaluation Data
The evaluation set is small. A larger labeled dataset would give a more reliable picture of retrieval quality.

## Summary

The current project is a strong prototype, but the next step is to improve robustness, retrieval quality, and deployment readiness.
