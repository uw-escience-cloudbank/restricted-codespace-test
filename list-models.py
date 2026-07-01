import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN"),
    base_url=os.environ.get("ANTHROPIC_BASE_URL")
)

models = client.models.list()
for model in models.data:
    print(model.id)
