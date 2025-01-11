class MemoryManager:
    def __init__(self):
        self.conversation_history = []

    def add_to_memory(self, question, answer):
        self.conversation_history.append(f"Q: {question}\nA: {answer}")

    def get_memory_context(self):
        return "\n".join(self.conversation_history)

    def clear_memory(self):
        self.conversation_history = []