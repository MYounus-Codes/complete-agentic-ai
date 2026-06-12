# Agentic AI Course: Building Practical AI Agents 🚀

Welcome to the **Agentic AI Course**! This repository contains hands-on tutorials, projects, and notebooks designed to take you from foundational LangChain concepts to building complex, autonomous, tool-using AI agents.

## 🛠️ Tech Stack & Tooling
- **Language:** Python 3.12+
- **Framework:** LangChain
- **LLM Provider:** Groq (High-speed inference)
- **Package Manager:** `uv` (Lightning-fast Python package management)
- **Data Validation:** Pydantic

---

## 📅 Course Curriculum

### 📂 Module 1: LangChain Foundations (`1_Langchain/`)
* **LangChain Introduction (`01_langchainintro.ipynb`):** Learn the core building blocks of LangChain, prompt templates, structured output parsing, and basic LLM interactions.
* **Weather Agent Project (`weatheragent_project.ipynb`):** Build a real-world, tool-using weather agent that connects with the OpenWeather API to provide real-time, validated weather data.
* **Web Search Agent (`websearch_agent.ipynb`):** Integrate web-search capabilities into your agents, enabling them to query the live internet, synthesize online sources, and answer current questions.

### 📂 Module 2: Retrieval-Augmented Generation (`2_RAG/`)
* *Coming Soon* - Implementing vector databases, semantic search, and context-aware agents.

### 📂 Module 3: Advanced & Deep Agents (`3_Deep_Agents/`)
* *Coming Soon* - High-autonomy agent architectures, memory management, and multi-agent coordination.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/agentic-ai-course.git
   cd agentic-ai-course
   ```

2. Sync the virtual environment and dependencies using `uv`:
   ```bash
   uv sync
   ```

3. Set up your environment variables (e.g., `GROQ_API_KEY`, `OPENWEATHER_API_KEY`) in a `.env` file.