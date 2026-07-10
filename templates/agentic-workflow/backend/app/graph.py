from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from app.llm import get_chat_model


@tool
def lookup_status(subject: str) -> str:
    """Look up the status of the given subject. Placeholder tool —
    code-agent replaces this with the project's real tool(s) per the
    approved plan; the graph wiring pattern stays the same."""
    return f"No real data source wired up yet for {subject!r} — replace this tool with a real lookup."


def build_agent():
    """Builds the project's LangGraph agent. Swap the tool list and prompt
    for the project's real capabilities; the create_react_agent wiring
    pattern is a reasonable default for a single-agent, tool-using graph."""
    model = get_chat_model()
    return create_react_agent(model, tools=[lookup_status])


def run_agent(input_text: str) -> dict:
    agent = build_agent()
    result = agent.invoke({"messages": [("user", input_text)]})
    messages = result["messages"]
    return {
        "final_answer": messages[-1].content,
        "trace": [
            {"type": type(m).__name__, "content": getattr(m, "content", None)}
            for m in messages
        ],
    }
