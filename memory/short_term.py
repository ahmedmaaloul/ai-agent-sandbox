class ShortTermMemory:
    def __init__(self):
        self.history = []

    def store(self, task, result):
        self.history.append((task, result))

    def retrieve(self):
        return self.history[-3:] if self.history else []
