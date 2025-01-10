import os
from loader.pdf_loader import load_documents_from_folder
from embeddings.generate_embeddings import generate_embeddings
from qa.qa_with_context import answer_question_with_context
from memory.memory_manager import MemoryManager

if __name__ == "__main__":
    # 动态获取文档文件夹路径
    folder_path = os.path.join(os.path.dirname(__file__), "documents")

    # Step 1: 加载文件夹中的文档内容
    try:
        docs = load_documents_from_folder(folder_path)
    except Exception as e:
        print(f"加载文档失败: {e}")
        exit(1)

    # Step 2: 生成嵌入并存储
    try:
        vector_store = generate_embeddings(docs)
    except Exception as e:
        print(f"生成嵌入失败: {e}")
        exit(1)

    # 初始化记忆模块
    memory_manager = MemoryManager()

    # Step 3: 用户提问并获取回答
    while True:
        question = input("请输入你的问题（输入'q'退出程序）：")
        if question.lower() == "q":
            break
        elif question.lower() == "clear":
            memory_manager.clear_memory()
            print("对话历史已清除。")
            continue
        try:
            answer = answer_question_with_context(question, vector_store, memory_manager)
            print(f"深蓝: {answer}")
        except Exception as e:
            print(f"回答问题时出错: {e}")
