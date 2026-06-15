# Evaluation Notes

## Dataset

The evaluation set contains 20 policy questions with expected document IDs for retrieval checking.

## Results

- Total questions: 20
- Retrieval hits: 12
- Retrieval accuracy: 60%

## Query Rewriting Comparison

- Rewriting off: 12/20 = 60.00%
- Rewriting on: 12/20 = 60.00%

Query rewriting did not improve retrieval on this dataset.

## What Worked Well

The system performed well on direct policy questions such as:
- travel reimbursement,
- meal allowance,
- leave policy,
- attendance policy,
- access control,
- MFA,
- incident reporting,
- acceptable use,
- software installation.

## What Failed

The system missed questions that were clearly outside the policy scope, such as:
- CEO home address,
- stock price,
- election outcome,
- salary,
- customer refund policy,
- cafeteria menu,
- company revenue,
- customer dress code.

## Interpretation

The results suggest the retrieval pipeline works reasonably well for in-scope employee policy questions but is not designed to answer unrelated or unsupported queries. That is expected for a policy-focused RAG system.

## Suggested Improvements

- Improve chunking strategy.
- Use a stronger reranker.
- Refine query routing.
- Add out-of-scope detection.
- Test an Azure-native retrieval stack.
