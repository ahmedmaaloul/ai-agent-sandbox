import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.base_agent import BaseAgent
from tools.file_writer import file_writer
from strategies.llm_strategy import LLMStrategy
from memory.short_term import ShortTermMemory

# The task for the agent
query = "Create a README file named 'demo_output.txt' with the text: 'This is a demo by Ahmed Maaloul.'"

# Instantiate the agent with file writing capability
agent = BaseAgent(
    name="FileBot",
    memory=ShortTermMemory(),
    tools=[file_writer],
    strategy=LLMStrategy()
)

# Run the task
response = agent.act(query)
print(f"\n🤖 Agent Response:\n{response}")
