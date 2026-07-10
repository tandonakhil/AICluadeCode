import os


def get_chat_model():
    """Returns a LangChain chat model for whichever provider is configured.

    LLM_PROVIDER switches the backing generation model. Note this is
    independent of embeddings (see embeddings.py) — Anthropic has no
    embeddings API, so retrieval always uses OpenAI embeddings regardless of
    which provider generates the final answer.
    """
    provider = os.environ.get("LLM_PROVIDER", "anthropic").lower()

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5"))

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model=os.environ.get("OPENAI_MODEL", "gpt-4o"))

    raise ValueError(f"Unknown LLM_PROVIDER: {provider!r} (expected 'anthropic' or 'openai')")
