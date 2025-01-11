from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def answer_question_with_context(question, vector_store, memory_manager, llm_model_name="qwen2.5:14b"):
    template = """Question: {question}
Context:
{context}
Answer: Answer me in Chinese"""
    prompt = ChatPromptTemplate.from_template(template)
    llm_model = OllamaLLM(model=llm_model_name)
    
    memory_context = memory_manager.get_memory_context()
    
    relevant_docs = vector_store.similarity_search(question, k=3)
    if not relevant_docs:
        return "No relevant content found. Please try changing the question."
    
    context = "\n".join([doc.page_content for doc in relevant_docs])
    if not context.strip():
        return "The retrieved context is empty. Maybe the document content was not loaded correctly or the question doesn't match."
    
    full_context = f"{memory_context}\n{context}"
    
    final_prompt = prompt.format(question=question, context=full_context)
    
    try:
        res = llm_model.invoke(final_prompt)
        memory_manager.add_to_memory(question, res)
        return res
    except Exception as e:
        return f"An error occurred while generating the answer: {e}"