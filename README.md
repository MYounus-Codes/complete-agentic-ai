# Agentic AI Course: Building Practical AI Agents

Welcome to the **Agentic AI Course**! This repository contains hands-on tutorials, notebooks, and projects that take you from Python fundamentals to building complex, autonomous, tool-using AI agents.

## Tech Stack & Tooling

- **Language:** Python 3.12+
- **Frameworks:** LangChain, DeepAgents
- **LLM Providers:** Groq, Google GenAI, OpenAI
- **Package Manager:** `uv` (lightning-fast Python package management)
- **Data Validation:** Pydantic

---

## Course Curriculum

### Module 0: Python Foundations (`00_python/`)

A self-paced Python curriculum covering the essentials needed before diving into AI agents.

| Topic | Topics Covered | Projects |
|---|---|---|
| **Basics** | Variables, conditionals, I/O | Number Story, Student Progress Tracker, Budget Planner |
| **Data Types** | Strings, lists, dicts, sets | Profile Card, Inventory Summary, Expense Report |
| **Functions** | Definitions, args, return values | Unit Converter, Text Toolkit, Recipe Planner |
| **Loops** | `for`, `while`, nested loops | Countdown Timer, Daily Menu Counter, Study Tracker |
| **OOP** | Classes, inheritance, encapsulation | Pet Demo, Bank Account System, School Management |

Each topic includes an `_intro.py` (examples), `_exercises.py` (practice), and three staged projects (`basic` / `medium` / `advanced`).

### Module 1: LangChain Foundations (`1_Langchain/`)

| Notebook | Description |
|---|---|
| `00_langchainintro` | Core building blocks: prompt templates, LLM interactions |
| `01_agents` | Introduction to agent architectures and reasoning loops |
| `02_models` | Working with different LLM providers and model parameters |
| `03_tools` | Creating and using custom tools with agents |
| `04_messages` | Chat message types, history, and conversation patterns |
| `05_structured_output` | Parsing and validating LLM outputs with Pydantic |

**Projects:**
- **Weather Agent** - Tool-using agent that fetches real-time weather data via OpenWeather API
- **Web Search Agent** - Internet-connected agent that queries live sources
- **Simple Website Builder** - Agent that generates static websites from natural language descriptions

### Module 2: Retrieval-Augmented Generation (`2_RAG/`)
*Coming soon* - Vector databases, semantic search, and context-aware RAG agents.

### Module 3: Advanced & Deep Agents (`3_Deep_Agents/`)
*Coming soon* - High-autonomy multi-agent systems, memory management, and agent coordination.

---

## Getting Started

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed
- Python 3.12+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/agentic-ai-course.git
   cd agentic-ai-course
   ```

2. Sync the virtual environment and dependencies:
   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root with your API keys:
   ```env
   GROQ_API_KEY=
   OPENWEATHER_API_KEY=
   GOOGLE_API_KEY=
   ```

### Running Notebooks

Launch Jupyter from the project root:
```bash
uv run jupyter notebook
```

Or run Python scripts directly:
```bash
uv run python 00_python/basics/basics_intro.py
```
