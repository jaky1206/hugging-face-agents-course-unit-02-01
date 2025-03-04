import os

from huggingface_hub import login
from dotenv import load_dotenv
from smolagents import load_tool, CodeAgent, HfApiModel

load_dotenv()
login(token=os.getenv("HF_TOKEN"))

image_generation_tool = load_tool(
    "m-ric/text-to-image",
    trust_remote_code=True
)

agent = CodeAgent(
    tools=[image_generation_tool],
    model=HfApiModel()
)

agent.run("Generate an image of a luxurious superhero-themed party at Wayne Manor with made-up superheros.")

# Sharing a Tool to the Hub
# party_theme_tool.push_to_hub("{your_username}/party_theme_tool", token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")