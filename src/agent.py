import os
import json
from dotenv import load_dotenv

from langchain import hub
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool, Tool
from langchain_core.prompts import ChatPromptTemplate

from openai import OpenAI
from langchain_openai import ChatOpenAI

from name_filter import extract_name
from gui import updating_chat_display, root

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

def top_imdb_result(query):
    name = extract_name(query)
    return google_search.results(name, 1)

def get_imdb_link(query):
    results = top_imdb_result(query)
    updating_chat_display('Calling IMDB Link Search for "' + query + '".', "calling_message")
    root.update()
    if results:
        return results[0].get("link", "")
    return ""

google_search = GoogleSearchAPIWrapper()

def calling_google_search(query):
    updating_chat_display('Calling Google Search for "' + query + '".', "calling_message")
    root.update()
    return google_search.run

tools = [
    Tool(
        name="imdb_link",
        description="Get the IMDb link URL for further information about the movie or TV series and its IMDb rating.",
        func=get_imdb_link,
    ),
    Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=calling_google_search,
    ),
    Tool(
        name="extract_name",
        description="Extract the name of the movie or TV series from the given question.",
        func=extract_name,
    )
]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are an AI assistant that provides accurate and concise information about movies and TV series. 
        Your primary role is to answer user queries using available knowledge and tools.

        **Instructions:**
        1. **Ensure Relevance**: 
           - Extract the movie or TV show name using the `extract_name` tool.
           - If a valid name is found, proceed.
           - Otherwise, respond: "Sorry, I only provide information about specific movies or TV series."

        2. **Fetch IMDb Details**:
           - Use the `imdb_link` tool to retrieve IMDb ratings.
           - If a rating is found, format it as: **"IMDb Rating: X.X/10"**.
           - If unavailable, explicitly state: **"IMDb rating not available."**

        3. **Use Google Search When Necessary**:
           - If your training data does not contain enough information to answer the question, use the `google_search` tool.
           - This is especially important for recent movies or TV shows that may not be included in your knowledge.

        4. **Response Format**:
           - Start with a short, relevant answer to the query.
           - Include IMDb rating when applicable.
           - If information was retrieved via Google Search, mention: **"(Source: Google Search)"**.
           - Keep responses brief and well-structured.

        Only answer questions related to movies and TV series.
        """),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def invoke_agent(user_input: str) -> str:
    result = agent_executor.invoke({"input": user_input})
    return result.get("output", "")
