import os


def get_chat_model():
    """Returns a LangChain chat model for whichever provider is configured.

    LLM_PROVIDER switches the backing model without touching call sites —
    every project built from this template can swap Anthropic/OpenAI via .env.
    """
    provider = os.environ.get("LLM_PROVIDER", "anthropic").lower()

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        # Default max_tokens (1024) was observed truncating real chat
        # responses mid-sentence during red-team testing on little-milestones
        # -- thinking-block overhead eats into that budget before the final
        # answer text is generated. Raised so guarded, disclaimer-bearing
        # answers have room to complete.
        return ChatAnthropic(
            model=os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5"),
            max_tokens=int(os.environ.get("ANTHROPIC_MAX_TOKENS", "4096")),
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model=os.environ.get("OPENAI_MODEL", "gpt-4o"))

    raise ValueError(f"Unknown LLM_PROVIDER: {provider!r} (expected 'anthropic' or 'openai')")
