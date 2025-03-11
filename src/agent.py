import os
import json
from dotenv import load_dotenv

from name_filter import extract_name

from langchain import hub
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool, Tool
from langchain_core.prompts import ChatPromptTemplate

from openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

def top_imdb_result(query):
    name = extract_name(query)
    return google_search.results(name, 1)

def get_imdb_link(query):
    results = top_imdb_result(query)
    if results:
        return results[0].get("link", "")
    return ""

google_search = GoogleSearchAPIWrapper()

tools = [
    Tool(
        name="imdb_link",
        description="Get the IMDb link URL for further information about the movie or TV series and its IMDb rating.",
        func=get_imdb_link,
    ),
    Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=google_search.run,
    )
]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are a knowledgeable and concise assistant specializing in providing information about movies and TV series. 
        Your responses should always include the IMDb rating when available.

        Instructions:
        1. Use the `imdb_link` tool to fetch the IMDb rating and relevant details.
        2. If the rating is unavailable, explicitly state: **"IMDb rating not available."**
        3. Structure your response as follows:
           - A short, clear answer to the user's question.
           - Followed by the IMDb rating in this exact format: **"IMDb Rating: X.X/10"**
        4. Only respond to questions about movies, TV series, or TV shows.
           - If the query is unrelated, reply: **"Sorry, I can only provide information about movies, TV series, and TV shows."**

        Keep responses concise, factual, and well-formatted.
        """),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def get_answer(user_input: str) -> str:
    result = agent_executor.invoke({"input": user_input})
    return result.get("output", "")
