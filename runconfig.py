from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv ,find_dotenv
load_dotenv(find_dotenv())
import os

gemini_api_key=os.getenv("GEMINI_API_KEY")

if not gemini_api_key :
    raise ValueError("Your Gemini_api_key is not defined.Please ensure it is defined in .env file")

external_client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)

provider=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config=RunConfig(
    model=provider,
    model_provider=external_client,
    tracing_disabled=True
      
)