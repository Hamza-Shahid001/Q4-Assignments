import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, set_default_openai_client, set_default_openai_api

# Load environment variables
load_dotenv()
# Set the API key from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

set_default_openai_api("chat_completions") # Set the default OpenAI API to chat completions

# Prompt for the user to input
prompt = input("Enter your prompt: ")

# Initialize the OpenAI client
external_client = AsyncOpenAI(
    api_key = API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_default_openai_client(external_client)
set_tracing_disabled(True)  # Disable tracing for cleaner output

agent = Agent(name="Assistant", instructions="Respond according to the prompt", model="gemini-2.0-flash")

result = Runner.run_sync(agent, input=prompt)
print(result.final_output)