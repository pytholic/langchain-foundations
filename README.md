# LangChain Foundations

A comprehensive hands-on exploration of LangChain's core capabilities, from foundational models to advanced multi-agent systems (2026).

## Topics Covered

### Module 1: Foundations
- **Foundational Models**: Chat models, prompting patterns, and structured outputs
- **Tools**: Web search integration (Tavily), function calling, and tool execution
- **Memory**: Conversation history, checkpointing, and state persistence
- **Multimodal Messages**: Image processing and vision capabilities
- **Project**: Personal Chef Agent with memory and tool use

### Module 2: Advanced Patterns
- **MCP (Model Context Protocol)**: Server integration, custom tools, and external data sources
- **Runtime Context**: Dynamic state management and tool runtime injection
- **State Management**: Custom state schemas and state updates with Commands
- **Multi-Agent Systems**: Agent coordination, delegation, and hierarchical workflows
- **Project**: Wedding Planner with specialized sub-agents (travel, venue, playlist)

### Module 3: Production Patterns
- **Managing Messages**: Message filtering, pruning, and context window optimization
- _(More topics coming soon)_

### LangSmith
We also look into LangSmith features to trace our agents workflow. This can be helpful for resource management, optimization, and error debugging.

## Quick Start

```bash
# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Add your API keys: OPENAI_API_KEY, GOOGLE_API_KEY, TAVILY_API_KEY

# Run notebooks
jupyter lab notebooks/
```

## Project Structure

```
notebooks/
├── module-1/
│   ├── 1.1_foundational_models.ipynb
│   ├── 1.1_prompting.ipynb
│   ├── 1.2_tools.ipynb
│   ├── 1.2_web_search.ipynb
│   ├── 1.3_memory.ipynb
│   ├── 1.4_multimodal_messages.ipynb
│   └── 1.5_personal_chef.ipynb
├── module-2/
│   ├── 2.1_mcp.ipynb
│   ├── 2.2_runtime_context.ipynb
│   ├── 2.2_state.ipynb
│   ├── 2.3_multi_agent.ipynb
│   ├── 2.4_wedding_planners.ipynb
│   └── resources/
│       ├── 2.1_mcp_server.py
│       └── Chinook.db
└── module-3/
    └── 3.2_managing_messages.ipynb
    ├── 3.3_human_in_the_loop.ipynb
    ├── 3.4_dynamic_prompts.ipynb
    ├── 3.4_dynamic_tools.ipynb
    ├── 3.4_dynamic_models.ipynb
    ├── 3.5_email_agent.ipynb
```

## Key Patterns

### Agent with Tools and Memory

```python
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
agent = create_agent(
    model=model,
    tools=[web_search, calculator],
    checkpointer=InMemorySaver(),
    system_prompt="You are a helpful assistant."
)

# With memory persistence
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather?"}]},
    config={"configurable": {"thread_id": "user-123"}}
)
```

### Multi-Agent Coordination

```python
# Coordinator delegates to specialized agents
@tool
def search_flights(runtime: ToolRuntime) -> str:
    """Delegate flight search to travel agent."""
    origin = runtime.state["origin"]
    destination = runtime.state["destination"]
    return await travel_agent.ainvoke({"messages": [...]})

coordinator = create_agent(
    model=model,
    tools=[search_flights, search_venues, suggest_playlist],
    state_schema=WeddingState
)
```

### MCP Server Integration

```python
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({
    "travel_server": {
        "transport": "streamable_http",
        "url": "https://mcp.kiwi.com"
    }
})

tools = await client.get_tools()
agent = create_agent(model=model, tools=tools)
```

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- API keys: Google Gemini (or any other provider), Tavily (for web search)

## Acknowledgement
This course is inspired by Langchain Academy.