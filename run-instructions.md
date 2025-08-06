# How to Run the Azure OpenAI Connection Test

This guide explains how to set up and run the `tests/test.py` script to verify your connection to Azure OpenAI.

## 1. Prerequisites

- Python 3.8+
- `uv` installed (or you can use `pip`)

## 2. Setup

### Create a `.env` file

Create a `.env` file in the root directory of the project with the following content. Replace the placeholder values with your actual Azure OpenAI credentials.

```
AZURE_OPENAI_API_KEY="your_api_key_here"
AZURE_OPENAI_ENDPOINT="your_endpoint_here"
AZURE_OPENAI_API_VERSION="your_api_version_here"
AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name_here"
```

### Install Dependencies

Install the required Python packages using `uv`:

```bash
uv pip install pytest pytest-asyncio python-dotenv openai
```

## 3. Running the Test

Execute the test using `pytest`:

```bash
pytest tests/test.py
uv run -m pytest tests/test.py
```

If the connection is successful and the setup is correct, the test should pass without errors.
