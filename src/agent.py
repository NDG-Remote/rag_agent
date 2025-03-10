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

google_search = GoogleSearchAPIWrapper()

def top_imdb_result(query):
    """Get the top IMDb result for a given query."""
    name = extract_name(query)
    return google_search.results(name, 1)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant to answer questions about movies and TV series. Please provide a brief answer to the question, crawl the content of the IMDB link provided by the tool and add the information about the current IMDb rating to this answer."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

@tool
def get_imdb_link(query):
    """Get the IMDb link for the top result of a given query."""
    results = top_imdb_result(query)
    if results:
        return results[0].get("link", "")
    return ""

tools = [get_imdb_link]

agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

def get_answer(user_input: str) -> str:
    result = agent_executor.invoke({"input": user_input})
    return result.get("output", "")
