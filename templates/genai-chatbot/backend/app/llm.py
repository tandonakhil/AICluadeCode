import os


def get_chat_model():
    """Returns a LangChain chat model for whichever provider is configured.

    LLM_PROVIDER switches the backing model without touching call sites —
    every project built from this template can swap Anthropic/OpenAI via .env.
    """
    provider = os.environ.get("LLM_PROVIDER", "anthropic").lower()

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5"))

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model=os.environ.get("OPENAI_MODEL", "gpt-4o"))

    raise ValueError(f"Unknown LLM_PROVIDER: {provider!r} (expected 'anthropic' or 'openai')")
