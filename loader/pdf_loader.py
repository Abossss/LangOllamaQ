import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents_from_folder(folder_path):
    """
    从指定文件夹加载所有 PDF 文档。
    :param folder_path: 文件夹路径
    :return: 包含所有文档内容的列表
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"文件夹路径无效: {folder_path}")
    
    docs = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):  # 扫描 PDF 文件
                file_path = os.path.join(root, file)
                try:
                    loader = PyPDFLoader(file_path)
                    file_docs = loader.load()
                    docs.extend(file_docs)
                    print(f"成功加载文件: {file_path}, 共 {len(file_docs)} 页")
                except Exception as e:
                    print(f"加载文件 {file_path} 失败: {e}")
    if not docs:
        raise RuntimeError("未找到任何可加载的 PDF 文档。")
    
    print(f"总共加载 {len(docs)} 页文档内容。")
    return docs
