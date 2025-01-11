import os
from loader.pdf_loader import load_documents_from_folder
from embeddings.generate_embeddings import generate_embeddings
from qa.qa_with_context import answer_question_with_context
from memory.memory_manager import MemoryManager

if __name__ == "__main__":
    folder_path = os.path.join(os.path.dirname(__file__), "documents")

    try:
        docs = load_documents_from_folder(folder_path)
    except Exception as e:
        print(f"Failed to load documents: {e}")
        exit(1)

    try:
        vector_store = generate_embeddings(docs)
    except Exception as e:
        print(f"Failed to generate embeddings: {e}")
        exit(1)

    memory_manager = MemoryManager()

    while True:
        question = input("Please enter your question (enter 'q' to quit the program):")
        if question.lower() == "q":
            break
        elif question.lower() == "clear":
            memory_manager.clear_memory()
            print("Conversation history has been cleared.")
            continue
        try:
            answer = answer_question_with_context(question, vector_store, memory_manager)
            print(f"DeepBlue: {answer}")
        except Exception as e:
            print(f"An error occurred while answering the question: {e}")