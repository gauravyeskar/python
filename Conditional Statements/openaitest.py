# API calling
import load_dotenv
import openai
from dotenv import load_dotenv
# from .env import apikey
import os

# Load key from .env
load_dotenv()
# api_key = os.getenv("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")
# api_key = os.getenv("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")
api_key = os.getenv('https://platform.openai.com/apikey')
client = openai.OpenAI(api_key = api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message.content.strip())