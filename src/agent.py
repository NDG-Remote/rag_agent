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

from gui import updating_chat_display, root
from imdb_api import get_imdb_api_data

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

def run_agent(user_input, name):
    def fetch_imdb_api_data(name):
        updating_chat_display("Calling IMDb API for the movie/TV series.", "calling_message")
        root.update()
        return get_imdb_api_data(name)

    google_search = GoogleSearchAPIWrapper()

    def calling_google_search(query):
        updating_chat_display("Calling Google Search for \"" + query + "\".", "calling_message")
        root.update()
        return google_search.run

    tools = [
        Tool(
            name="imdb_data",
            description="Get the data in a dictionary of the queried movie or tv-show.",
            func=fetch_imdb_api_data,
        ),
        Tool(
            name="google_search",
            description="Search Google for recent results.",
            func=calling_google_search,
        )
    ]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
        You are an AI assistant specializing in providing accurate and concise information about movies and TV series.

        **Instructions:**
        1. **Always Retrieve IMDb Data First:**
           - Always call the `imdb_data` tool to fetch details before answering.
           - Extract only the IMDb rating and release date.
           - Always include the IMDb rating, if available, in this format in the last sentence of the answer.
           - If the release date is available, include it naturally in your response.
           - If there is no IMDb data, respond using your training data.

        2. **Use Google Search When Necessary:**
           - If IMDb data is insufficient to answer the question fully, call the `google_search` tool.
           - Make sure that, if the question is about a recent movie or TV show, use `google_search` to ensure up-to-date information.
           - Make sure that, if your training data does not contain the answer, use `google_search` to find relevant results.
           - Clearly indicate when information is sourced from Google: **"(Source: Google Search)"**.

        3. **Response Format:**
           - Answer the question concisely.
           - Always include the IMDb rating and release date when available.
           - Only provide extra details (budget, runtime, genres, etc.) if explicitly asked.
           - Keep responses well-structured and conversational.

        **Important Rules:**
        - Always call the `imdb_data` tool first.
        - Only use `google_search` if IMDb data is missing or outdated.
        - If IMDb data is available, assume the question is about a movie or TV series.
        - If you cannot find an answer, respond politely without making up information.

        Only answer questions related to movies and TV series. If you can't give an answer, say so politely.
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

    return invoke_agent(user_input)
