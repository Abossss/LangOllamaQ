class MemoryManager:
    """
    用于管理对话历史的记忆模块。
    """
    def __init__(self):
        # 初始化对话历史存储
        self.conversation_history = []

    def add_to_memory(self, question, answer):
        """
        添加新的对话记录到记忆中。
        :param question: 用户的问题
        :param answer: 模型的回答
        """
        self.conversation_history.append(f"Q: {question}\nA: {answer}")

    def get_memory_context(self):
        """
        获取完整的对话上下文。
        :return: 历史对话拼接成的字符串
        """
        return "\n".join(self.conversation_history)

    def clear_memory(self):
        """
        清除对话历史。
        """
        self.conversation_history = []
