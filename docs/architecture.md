# Architecture

## Overview

Employee Policy Copilot is a retrieval-augmented generation (RAG) system for answering employee policy questions from internal policy documents. The pipeline combines keyword retrieval, dense retrieval, routing, reranking, and grounded answer generation.

## Main Components

### 1. Document Loader
The loader reads `.txt` policy files from the documents folder and attaches metadata such as file name, folder, and file path.

### 2. Chunking
Long policy documents are split into overlapping text chunks. This improves retrieval quality by allowing the system to match smaller, more focused pieces of text.

### 3. Dense Embeddings
Each chunk is converted into a vector embedding using a sentence transformer model. These embeddings support semantic search.

### 4. BM25 Retrieval
A BM25 index is built over the chunk text. This provides keyword-based retrieval for exact or near-exact term matching.

### 5. Query Router
The router classifies queries into groups such as HR, finance, IT, compliance, keyword-heavy, or general. It adjusts retrieval behavior based on the query type.

### 6. Hybrid Retrieval
The system combines BM25 scores and dense similarity scores into a single ranked list. This improves recall compared with keyword search alone.

### 7. Reranker
A lightweight reranker adjusts the top retrieved chunks using word overlap and length penalty. This helps improve the final ordering.

### 8. Answer Generation
The top retrieved chunks are passed to NVIDIA NIM. The generator answers only from the provided policy context.

### 9. Evaluation
The evaluation pipeline measures retrieval hit rate against labeled ground-truth document IDs. It also saves results for later inspection.

## Data Flow

User query  
→ optional query rewriting  
→ query routing  
→ hybrid retrieval  
→ reranking  
→ answer generation  
→ evaluation output

## Current Behavior

- Query rewriting is optional.
- Retrieval is evaluated on 20 labeled questions.
- The current retrieval accuracy is 60%.
- Rewriting did not improve retrieval accuracy on this dataset.

## Design Notes

The project is intentionally modular so each step can be tested or replaced independently. The notebook version is useful for experimentation, while the `src/` folder contains reusable code for a proper repo structure.
