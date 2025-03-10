import os
from dotenv import load_dotenv

from PIL import Image
import requests
from io import BytesIO
from smolagents import CodeAgent, OpenAIServerModel

load_dotenv()

image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/e/e8/The_Joker_at_Wax_Museum_Plus.jpg", # Joker image
    "https://upload.wikimedia.org/wikipedia/en/9/98/Joker_%28DC_Comics_character%29.jpg" # Joker image
]

images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    images.append(image)

model = OpenAIServerModel(
    model_id=os.getenv("OPENAI_API_MODEL_ID"),
    api_base=os.getenv("OPENAI_API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Instantiate the agent
agent = CodeAgent(
    tools=[],
    model=model,
    max_steps=20,
    verbosity_level=2
)

response = agent.run(
    """
    Describe the costume and makeup that the comic character in these photos is wearing and return the description.
    Tell me if the guest is The Joker or Wonder Woman.
    """,
    images=images
)