# ai — LLM & RAG & AI Agents

A compact repository for learning retrieval‑augmented generation (RAG) and multi‑agent AI workflows using LangGraph. Code is handcrafted and used for experimenting with real examples and tests — no AI‑generated code is included.

Books / references used:

<table>
  <tr>
    <td><img src="media/build_llm_from_scratch.png" alt="Build LLM From Scratch" width="240" /></td>
    <td><img src="media/generative_ai_with_langchain.png" alt="Generative AI with LangChain" width="240" /></td>
    <td><img src="media/learning_langchain.png" alt="Learning LangChain" width="240" /></td>
  </tr>
</table>

Short notes
- See `langgraph_agents/` for agent examples
- `rag/` for RAG utilities

- Environment: set OPENAI_API_KEY in a .env file and run examples directly.
- ├── .github
    └── copilot-instructions.md
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── README.md
├── __init__.py
├── agentic_rag
    ├── adaptive_rag.ipynb
    └── corrective_rag.ipynb
├── commands
├── langgraph_agents
    ├── __init__.py
    ├── data_analyst_agent.py
    ├── pandas_dataframe_agent.py
    └── router_query_classifier_agent.py
├── main.py
├── media
    ├── build_llm_from_scratch.png
    ├── generative_ai_with_langchain.png
    └── learning_langchain.png
├── pyproject.toml
├── rag
    └── pg_vector_stores.py
└── uv.lock
