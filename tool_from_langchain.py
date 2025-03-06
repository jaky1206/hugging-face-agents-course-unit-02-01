# could not test as SERPAPI_API_KEY is not available at this moment

import os

from huggingface_hub import login
from dotenv import load_dotenv
from langchain.agents import load_tools
from smolagents import CodeAgent, HfApiModel, Tool

load_dotenv()
login(token=os.getenv("HF_TOKEN"))

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

search_tool = Tool.from_langchain(load_tools(["serpapi"], serpapi_api_key=os.getenv("SERPAPI_API_KEY"))[0])

agent = CodeAgent(tools=[search_tool], model=model)

agent.run("Search for luxury entertainment ideas for a superhero-themed event, such as live performances and interactive experiences.")
