import os
import json
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from openai import AsyncAzureOpenAI
from agents import Agent, Runner, set_default_openai_client, set_tracing_export_api_key, set_tracing_disabled
from music_studio.agents.composer.schema import ComposerOutput

load_dotenv()

azure_openai_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

set_default_openai_client(azure_openai_client)
set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))
set_tracing_disabled(False)

env = Environment(loader=FileSystemLoader('api-ai-music-studio/src/music_studio/agents/composer'))
template = env.get_template('prompt.jinja')

user_prompt = "create new song"
rendered_prompt = template.render(user_prompt=user_prompt)

composer_agent = Agent(
    name="Composer",
    instructions="",
    model="gpt-4.1",
)

response = Runner.run_sync(composer_agent, rendered_prompt)

try:
    result_json = json.loads(response.final_output)
    validated_output = ComposerOutput.model_validate(result_json)
    print("Validated Composer Output:", validated_output)
except (json.JSONDecodeError, Exception) as e:
    print("Error parsing/validating output:", e)
