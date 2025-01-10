from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

def generate_embeddings(docs, embedding_model_name="nomic-embed-text:latest"):
    """生成文本嵌入并存储到向量存储中"""
    embeddings_model = OllamaEmbeddings(model=embedding_model_name)
    vector_store = InMemoryVectorStore(embeddings_model)
    
    for doc in docs:
        page_content = doc.page_content
        vector_store.add_texts([page_content])  # 添加每页内容的嵌入
    print(f"成功生成嵌入，并存储 {len(docs)} 页文档内容")
    return vector_store
