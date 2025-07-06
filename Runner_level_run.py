import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from agents.run import RunConfig

# Load environment variables
load_dotenv()
# Set the API key from environment variables
my_api_key = os.getenv("GEMINI_API_KEY")

# Prompt for the user to input
prompt = input("Enter your prompt: ")

# Initialize the OpenAI client
external_client = AsyncOpenAI(
    api_key = my_api_key,  # Replace with your actual API key
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the agent with instructions

simple_agent:Agent = Agent(
    name = "Personal Assistant",
    instructions = "Respond according to the prompt",
)

async def main():
    result = await Runner.run(simple_agent, input=prompt, run_config=config)
    print(result.final_output)

asyncio.run(main())