import os
from dotenv import load_dotenv

import requests

from openai import OpenAI

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = """Extract the name of the movie or TV series from the given question.
The output should be a string containing only the title, with proper capitalization and no extra words.
Examples:
- What do you know about the movie Matrix? → 'The Matrix'
- In Pretty Woman, who is the protagonist? → 'Pretty Woman'
- How long is the movie Vanilla Sky? → 'Vanilla Sky'
- How many chapters does the second season of Game of Thrones have? → 'Game of Thrones'
- In which year was the movie Inseption released? → 'Inception'
- What is the Spanish title of the movie 'Die Hard'? → 'Die Hard'
- How many movies does the series fast and the furious have? → 'The Fast and the Furious'.
- When does the movie A Big Bold Beautiful Journey come out? → 'A Big Bold Beautiful Journey'

Ensure that:
- The extracted title is formatted correctly.
- Common variations like 'movie,' 'film,' or 'series' are ignored.
- If quotes are present, extract only the content inside them.
- Correct common spelling mistakes in well-known titles.
- If you can't find the movie or TV series, return an empty string.
"""

def extract_name(question: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
        ],
        model="gpt-4o"
    )
    return chat_completion.choices[0].message.content