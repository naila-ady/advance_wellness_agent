
from openai.types.responses import ResponseTextDeltaEvent

async def stream_agent_response(result):
    """Stream the LLM response live to the terminal."""
    full_response = ""
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            delta = event.data.delta
            print(delta, end="", flush=True)
            full_response += delta
    print()
    return full_response
