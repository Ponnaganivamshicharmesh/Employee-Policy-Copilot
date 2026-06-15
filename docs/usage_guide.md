# Usage Guide

## Prerequisites

- Python 3.10 or newer.
- Google Colab or a local environment with the required packages.
- NVIDIA API key stored in Colab secrets or environment variables.
- Policy documents placed in the correct `data/documents/` folder.

## Colab Setup

1. Mount Google Drive.
2. Install dependencies.
3. Load documents and metadata.
4. Build chunks, embeddings, and BM25 index.
5. Run the query pipeline.
6. Run evaluation.
7. Save outputs to Google Drive.

## Running the Project

### In Colab
- Open the notebook.
- Run all cells in order.
- Ensure `PROJECT_ROOT` points to your Drive folder.
- Set `NVIDIA_API_KEY` in Colab secrets.
- Save evaluation outputs into the Drive-based `outputs/` folder.

### In VS Code
- Open the repo folder.
- Install dependencies with `pip install -r requirements.txt`.
- Run the scripts or notebook locally.
- Keep the data folder structure unchanged.

## Output Files

The evaluation step saves:
- `evaluation_results.csv`
- `evaluation_summary.json`
- `sample_answers.txt`

These files are stored under:
- `outputs/rewrite_off/`
- `outputs/rewrite_on/`

## Troubleshooting

- If the notebook cannot find the documents, check the `PROJECT_ROOT` path.
- If NVIDIA API calls fail, verify the API key.
- If GitHub shows an invalid notebook error, clear notebook outputs and remove widget metadata.
- If output files are missing in Colab, confirm they were saved to Drive and not only the runtime filesystem.
