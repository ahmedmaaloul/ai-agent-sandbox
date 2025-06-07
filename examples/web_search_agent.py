from agents.base_agent import BaseAgent
from tools.web_search import web_search
from strategies.llm_strategy import LLMStrategy
from memory.short_term import ShortTermMemory

query = "Who is the current director of ESILV?"

agent = BaseAgent(
    name="WebSearchBot",
    memory=ShortTermMemory(),
    tools=[web_search],
    strategy=LLMStrategy()
)

response = agent.act(query)
print(f"\n🤖 Agent Response:\n{response}")