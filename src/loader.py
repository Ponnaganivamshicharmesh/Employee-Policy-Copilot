from typing import List, Dict
import os
import glob
import json


class Document:
    def __init__(self, content: str, metadata: Dict = None):
        self.content = content
        self.metadata = metadata or {}


def load_documents_from_folder(folder_path: str) -> List[Document]:
    documents = []
    txt_files = glob.glob(os.path.join(folder_path, "**", "*.txt"), recursive=True)

    for txt_file in txt_files:
        with open(txt_file, "r", encoding="utf-8") as f:
            content = f.read()

        file_name = os.path.basename(txt_file)
        folder_name = os.path.basename(os.path.dirname(txt_file))

        documents.append(
            Document(
                content=content,
                metadata={
                    "file_name": file_name,
                    "folder": folder_name,
                    "file_path": txt_file,
                    "content_length": len(content),
                },
            )
        )

    return documents


def load_json_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)