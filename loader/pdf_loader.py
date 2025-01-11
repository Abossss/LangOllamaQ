import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents_from_folder(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Invalid folder path: {folder_path}")
    
    docs = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    loader = PyPDFLoader(file_path)
                    file_docs = loader.load()
                    docs.extend(file_docs)
                    print(f"Successfully loaded file: {file_path}, with {len(file_docs)} pages")
                except Exception as e:
                    print(f"Failed to load file {file_path}: {e}")
    if not docs:
        raise RuntimeError("No loadable PDF documents found.")
    
    print(f"Totally loaded {len(docs)} pages of document content.")
    return docs
    