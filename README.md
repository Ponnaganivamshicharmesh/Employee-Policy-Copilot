# Employee Policy Copilot

A hybrid Retrieval-Augmented Generation (RAG) system for answering employee policy questions from internal policy documents.

## Overview

This project builds a policy copilot that retrieves relevant policy chunks using BM25 + dense embeddings, optionally rewrites queries, reranks results, and generates grounded answers using NVIDIA NIM.

## Features

- Loads policy documents from a structured folder.
- Chunks long documents into overlapping text segments.
- Uses hybrid retrieval with BM25 and sentence embeddings.
- Adds query routing for department-aware retrieval.
- Supports optional query rewriting.
- Includes lightweight reranking.
- Generates answers from retrieved policy context.
- Evaluates retrieval performance on a labeled QA set.

## Tech Stack

- Python
- Google Colab
- PyTorch
- Sentence Transformers
- Rank-BM25
- scikit-learn
- NVIDIA NIM
- LangChain utilities

## Project Structure

```text
employee-policy-copilot/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
├── src/
├── data/
├── outputs/
└── docs/
```

## How It Works

1. Load policy documents and metadata.
2. Split documents into overlapping chunks.
3. Create dense embeddings for chunks.
4. Build a BM25 index for keyword retrieval.
5. Route the query based on its type.
6. Retrieve candidates using hybrid search.
7. Rerank the top results.
8. Generate a grounded answer from the best chunks.

## Evaluation

The system was evaluated on 20 policy questions.

- Retrieval accuracy without query rewriting: 60.00%
- Retrieval accuracy with query rewriting: 60.00%

## Setup

```bash
git clone https://github.com/your-username/employee-policy-copilot.git
cd employee-policy-copilot
pip install -r requirements.txt
```

## Configuration

Set your NVIDIA API key before running generation:

```bash
export NVIDIA_API_KEY="your_key_here"
```

## Usage

Run the notebook or the main pipeline script after placing the documents and metadata in the `data/` directory.

## Results

This project demonstrates a practical hybrid RAG pipeline for enterprise policy search and answer generation.

## Future Improvements

- Better query routing.
- Improved chunking strategy.
- Stronger reranking model.
- Azure-native deployment.
- Web UI for employee search.

## Author

Your Name
