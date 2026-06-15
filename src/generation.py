import os
import requests


class NVIDIAAnswerGenerator:
    def __init__(self, model_name="meta/llama-3.3-70b-instruct", api_key=None):
        self.model_name = model_name
        self.api_key = api_key or os.environ.get("NVIDIA_API_KEY", "")
        self.api_url = "https://integrate.api.nvidia.com/v1/chat/completions"

    def generate(self, query, documents, max_length=500):
        if not documents:
            return "No relevant documents found for your query."

        context = "\n\n".join([doc_score_tuple[0].content for doc_score_tuple in documents[:3]])

        prompt = (
            "Answer the user question using only the policy context below.\n"
            "If the context does not contain the answer, say you do not have enough information.\n\n"
            f"Policy context:\n{context}\n\n"
            f"User question:\n{query}"
        )

        response = requests.post(
            self.api_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": "You answer only from the provided policy context."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
                "top_p": 0.9,
                "max_tokens": max_length,
                "stream": False,
            },
            timeout=120,
        )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()

        return f"API error ({response.status_code}): {response.text}"