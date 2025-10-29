# AI Coding Guidelines for LangGraph Agent Project

## Architecture Overview
This project builds AI agents using LangGraph for workflow orchestration. The core pattern uses `StateGraph` with `TypedDict` states containing annotated message lists for conversation tracking.

**Key Components:**
- `langgraph_agents/`: Contains specialized agents (query routing, SQL generation, pandas analysis)
- `rag/`: Retrieval-augmented generation components (currently minimal)
- State-driven workflows with conditional edges for domain routing

## Agent Patterns

### StateGraph Structure
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history
    user_query: str  # Input
    # ... domain-specific outputs

builder = StateGraph(State, input=Input, output=Output)
builder.add_node("node_name", node_function)
builder.add_conditional_edges("router", pick_retriever)
```

### Temperature Strategy
- **Low temperature (0.1)**: Structured tasks (SQL generation, routing, parsing)
- **High temperature (0.7)**: Creative tasks (explanations, natural language responses)

### Domain Routing
Use conditional edges for routing queries between domains (e.g., medical records vs insurance FAQs). Always include domain classification in state.

## Development Workflow

### Environment Setup
```bash
uv sync  # Install dependencies from uv.lock
```

### Code Quality
- Pre-commit hooks run Ruff linter and formatter automatically
- Ruff config in `pyproject.toml` ignores F401, E402, F841 (unused imports, import order, unused variables)

### Testing Agents
Agents include inline test invocations at file bottom:
```python
result = graph.invoke({"user_query": "sample query"})
print("Output:", result["output_field"])
```

## Key Conventions

### Import Pattern
```python
from dotenv import load_dotenv
import os
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
```

### Vector Stores
Use `InMemoryVectorStore` for development/testing. Initialize empty and populate as needed:
```python
store = InMemoryVectorStore.from_documents([], embeddings)
retriever = store.as_retriever()
```

### Message Handling
Use `HumanMessage` for user input, `SystemMessage` for prompts. Add messages to state for conversation continuity.

## Dependencies
- **LangChain ecosystem**: Core orchestration, OpenAI integration, experimental tools
- **LangGraph**: Agent workflow management
- **OpenAI**: GPT-4o-mini with domain-specific prompting
- **python-dotenv**: Environment variable management

## File Organization
- `langgraph_agents/`: One agent per file with complete runnable examples
- `rag/`: Vector store implementations
- Root level: Configuration files (pyproject.toml, uv.lock, .pre-commit-config.yaml)

## Common Patterns
- TypedDict states with message annotation: `Annotated[list, add_messages]`
- Router nodes for domain classification
- Separate generation and explanation nodes in multi-step workflows
- Inline testing with `graph.invoke()` calls</content>
<parameter name="filePath">c:\Users\re_zi\github_projects\ai\.github\copilot-instructions.md