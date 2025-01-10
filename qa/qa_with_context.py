from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def answer_question_with_context(question, vector_store, memory_manager, llm_model_name="qwen2.5:14b"):
    """
    基于上下文和问题生成答案，同时支持历史记忆。
    :param question: 用户提问
    :param vector_store: 向量数据库实例
    :param memory_manager: MemoryManager 实例，用于管理记忆
    :param llm_model_name: 使用的语言模型名称
    """
    # 初始化 LLM 和 Prompt 模板
    template = """Question: {question}
Context:
{context}
Answer: 用中文回答我"""
    prompt = ChatPromptTemplate.from_template(template)
    llm_model = OllamaLLM(model=llm_model_name)
    
    # 获取对话历史上下文
    memory_context = memory_manager.get_memory_context()
    
    # 从向量数据库中检索与问题相关的内容
    relevant_docs = vector_store.similarity_search(question, k=3)
    if not relevant_docs:
        return "未找到相关内容，请尝试更改问题。"
    
    # 提取上下文
    context = "\n".join([doc.page_content for doc in relevant_docs])
    if not context.strip():
        return "检索到的上下文为空，可能文档内容未正确加载或问题不匹配。"
    
    # 拼接问题、历史对话和检索到的上下文
    full_context = f"{memory_context}\n{context}"
    
    # 拼接问题和上下文
    final_prompt = prompt.format(question=question, context=full_context)
    
    # 生成回答
    try:
        res = llm_model.invoke(final_prompt)
        # 保存当前的对话到记忆
        memory_manager.add_to_memory(question, res)
        return res
    except Exception as e:
        return f"生成回答时出错: {e}"
