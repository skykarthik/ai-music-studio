#script to instantiate the composer agent

import os
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from agents import Agent, HandoffInputData, Runner, function_tool, handoff, trace, set_default_openai_client,set_default_openai_api, set_tracing_disabled, OpenAIChatCompletionsModel, set_tracing_export_api_key, add_trace_processor

load_dotenv()

azure_openai_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    #model=os.getenv("AZURE_OPENAI_MODEL"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

openai_client = azure_openai_client
set_default_openai_client(openai_client)
set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))
set_tracing_disabled(False)

composer_agent = Agent(
    name="Composer",
    instructions="",
    model = "gpt-4.1"
)

response = Runner.run_sync(composer_agent, "create new song")
print(response.final_output)