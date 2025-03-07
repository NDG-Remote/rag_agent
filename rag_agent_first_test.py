import os
from dotenv import load_dotenv

import requests

from openai import OpenAI

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

system_prompt = "You are a friendly and supportive teaching assistant for CS50 who is also a duck."

user_prompt = input("What's your question? ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    model="gpt-4o"
)

response_text = chat_completion.choices[0].message.content
print(response_text)