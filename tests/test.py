import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

# Load environment variables from .env file
load_dotenv()


async def main():
    """Tests the Azure OpenAI client chat completions API."""
    try:
        # Initialize the aysnc Azure OpenAI client
        client = AsyncAzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )

        # Create a chat completion request
        print("Sending request to Azure OpenAI...")
        response = await client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a creative storyteller."},
                {
                    "role": "user",
                    "content": "Write a short story about a robot who discovers music.",
                },
            ],
        )

        # Print the response
        print("\nResponse from Azure OpenAI:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Run the async function
    asyncio.run(main())
