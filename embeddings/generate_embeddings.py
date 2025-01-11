from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

def generate_embeddings(docs, embedding_model_name="nomic-embed-text:latest"):
    embeddings_model = OllamaEmbeddings(model=embedding_model_name)
    vector_store = InMemoryVectorStore(embeddings_model)
    
    for doc in docs:
        page_content = doc.page_content
        vector_store.add_texts([page_content])
    print(f"Embeddings generated and {len(docs)} pages of document content stored successfully")
    return vector_store
    