import os
from dotenv import load_dotenv
from huggingface_hub import login

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

load_dotenv()
login(token=os.getenv("HF_TOKEN"))

# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the model
model = HfApiModel()

agent = CodeAgent(
    model=model,
    tools=[search_tool]
)

# Example usage
response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)
print(response)