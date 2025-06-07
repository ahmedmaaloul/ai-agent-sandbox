# 🤖 AI Agent Sandbox Framework

A modular Python framework to build, test, and extend intelligent agents with memory, tools, and strategy. Inspired by AutoGPT and LangChain, this project gives developers full control with minimal overhead.

## 🚀 Features

- Plug & play AI agents with memory and tool usage
- Strategy layer powered by LLMs or custom logic
- Extensible tool system (web search, file reader, code executor, etc.)
- Simple CLI to simulate agent runs
- Examples included

## 📦 Requirements

- Python 3.8+
- OpenAI API key (or your own LLM)
- Optionally: DuckDuckGo Search API for local search

### Install dependencies:

```bash
pip install -r requirements.txt
````

### Set up your environment:

```bash
cp .env.example .env
```

## 🔧 Folder Structure

| Folder        | Description                     |
| ------------- | ------------------------------- |
| `agents/`     | Core agent logic                |
| `tools/`      | Modular tools for agents        |
| `strategies/` | Decision engines (e.g. LLMs)    |
| `memory/`     | Memory modules for agents       |
| `examples/`   | Agent demos                     |
| `cli.py`      | Interactive shell (coming soon) |

## 🧪 Try It

```bash
python examples/web_search_agent.py
```

## 📚 Coming Soon

* Streamlit visual dashboard
* Multi-agent support
* More tools: file writer, summarizer, calculator, etc.

## 🛠️ License

MIT
