import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load environment variables
load_dotenv()

# Set the API key from environment variables
my_api_key = os.getenv("GEMINI_API_KEY") # Replace with your actual API key

# Prompt for the user to input
prompt = input("Enter your prompt: ")

# Initialize the OpenAI client
external_client = AsyncOpenAI(
    api_key = my_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_tracing_disabled(True)  # Disable tracing for cleaner output

# Define the agent with instructions
async def main(
        simple_agent = Agent(
            name = "Personal Assistant",
            instructions = "Respond according to the prompt",
            model = OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client = external_client)
        )
    ):

    result = await Runner.run(simple_agent, input=prompt)
    print(result.final_output)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
