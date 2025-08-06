import os
import pytest
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

load_dotenv()

@pytest.mark.asyncio
async def test_azure_openai_connection():
    """
    Tests the connection to Azure OpenAI by sending a simple prompt.
    """
    # Load credentials from .env file
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    # Ensure all required environment variables are set
    assert api_key, "AZURE_OPENAI_API_KEY is not set in the .env file."
    assert azure_endpoint, "AZURE_OPENAI_ENDPOINT is not set in the .env file."
    assert api_version, "AZURE_OPENAI_API_VERSION is not set in the .env file."
    assert azure_deployment, "AZURE_OPENAI_DEPLOYMENT_NAME is not set in the .env file."

    # Initialize the client
    client = AsyncAzureOpenAI(
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
        azure_deployment=azure_deployment,
    )

    # Send a test prompt
    completion = await client.chat.completions.create(
        model="gpt-4.1",  # For Azure, this should be your deployment name
        messages=[
            {
                "role": "user",
                "content": "Say 'Hello!'",
            },
        ],
        max_tokens=10,
    )
    print(completion)
    # Assert that we got a response
    assert completion.choices[0].message.content is not None
    assert len(completion.choices[0].message.content) > 0
