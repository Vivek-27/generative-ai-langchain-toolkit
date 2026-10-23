# 🤖 Generative AI & LangChain Architecture Toolkit

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-v0.2+-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://langchain.com)
[![LCEL](https://img.shields.io/badge/LCEL-Runnables-black?style=flat-square)](https://python.langchain.com/docs/concepts/lcel/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

A hands-on, progressive engineering toolkit demonstrating **Generative AI architectures, LangChain Expression Language (LCEL), Prompt Engineering, Structured JSON Outputs, Dynamic Output Parsing, and RAG Document Ingestion Pipelines**.

---

## 🌟 Architecture & Modules Overview

This repository is structured progressively from foundational LLM calls to complex asynchronous parallel LCEL chains:

```
genai-learning/
│
├── 01_first_llm/             # LLM Initialization & Basic Prompt Chains
│   ├── 01_first_llm.py       # OpenAI / ChatModel connection & invocation
│   └── 02_prompt_chain.py    # Initial model chaining logic
│
├── 04_prompts/               # Prompt Engineering & System Directives
│   ├── 01_prompts.py         # PromptTemplate variable substitution
│   ├── 02_prompts.py         # Multi-variable context formatting
│   └── 03_chat_prompt.py     # SystemMessage, HumanMessage, AIMessage roles
│
├── 05_structured_output/     # Strict Schema Enforcement
│   └── 01_structured_output.py # Pydantic schema validation & tool calling
│
├── 06_output_parsers/        # Deterministic Parsing
│   ├── 01_output_parser.py   # StrOutputParser, JsonOutputParser
│   └── 02_output_parser.py   # CommaSeparatedListOutputParser
│
├── 07_chains/                # Multi-Step Reasoning Chains
│   └── 01_chain.py           # Sequential prompt-to-model-to-parser pipelines
│
├── 08_runnables/             # LangChain Expression Language (LCEL) Mastery
│   ├── 01_runnables.py       # Runnable interface fundamentals (invoke, batch, stream)
│   ├── 02_runnable_lambda.py # Custom data transformation with RunnableLambda
│   ├── 03_runnable_sequence.py# Pipe operator (|) compositional chaining
│   ├── 04_runnable_parallel.py# Parallel branch execution with RunnableParallel
│   └── 05_runnable_passthrough.py# Context propagation with RunnablePassthrough
│
└── 09_document_loaders/      # RAG Data Ingestion & Preprocessing
    ├── 01_text_loader.py     # Text file parsing
    ├── 03_text_lazyload.py   # Memory-efficient lazy loading for large corpora
    ├── 04_directory_loader.py# Recursive directory scanning & batch loading
    └── 05_web_loader.py      # Web scraping & URL document parsing with WebBaseLoader
```

---

## ⚡ LCEL Pipeline Demonstration

LangChain Expression Language (LCEL) powers deterministic, production-grade LLM workflows:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# LCEL Composition: Prompt | Model | Parser
prompt = ChatPromptTemplate.from_template("Explain {topic} in 2 sentences.")
model = ChatOpenAI(model="gpt-4o", temperature=0.7)
parser = StrOutputParser()

# Modern Runnable Chain
chain = {"topic": RunnablePassthrough()} | prompt | model | parser
response = chain.invoke("Distributed Systems")
print(response)
```

---

## 🚀 Getting Started

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/Vivek-27/generative-ai-langchain-toolkit.git
cd generative-ai-langchain-toolkit

# Create and activate virtual environment
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

### 3. Run Any Module

```bash
python 08_runnables/04_runnable_parallel.py
```

---

## 🛠️ Tech Stack

- **Framework:** LangChain, LangChain-Core, LangChain-Community, LangChain-OpenAI
- **LLM Providers:** OpenAI (GPT-4o, GPT-3.5), HuggingFace Hub
- **Core Concepts:** LCEL, Runnables (`RunnableSequence`, `RunnableParallel`), Document Loaders, Pydantic, Prompt Engineering

---

## 👨‍💻 Author

- **Vivek Kumar** — [LinkedIn](https://www.linkedin.com/in/vivek-fullstack/) • [GitHub](https://github.com/Vivek-27)
