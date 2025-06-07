class BaseAgent:
    def __init__(self, name, memory, tools, strategy):
        self.name = name
        self.memory = memory
        self.tools = {tool.__name__: tool for tool in tools}
        self.strategy = strategy

    def act(self, task: str) -> str:
        context = self.memory.retrieve()
        decision = self.strategy.plan(task, list(self.tools.keys()), context)
        if decision["tool"] in self.tools:
            result = self.tools[decision["tool"]](**decision["args"])
            self.memory.store(task, result)
            return result
        return "No valid tool selected."
