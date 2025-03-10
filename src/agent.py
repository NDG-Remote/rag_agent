import os
from dotenv import load_dotenv

from langchain import hub
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain_core.tools import Tool

load_dotenv()

os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

google_search = GoogleSearchAPIWrapper()

google_tool = Tool(
    name="google-search",
    description="Search Google for recent results.",
    func=google_search.run,
)

llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta")
chat_model = ChatHuggingFace(llm=llm)
prompt = hub.pull("hwchase17/structured-chat-agent")

agent = create_structured_chat_agent(
    llm=chat_model,
    tools=[google_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[google_tool],
    verbose=True,
    handle_parsing_errors=True,
    max_interactions=5
)

agent_executor.invoke({"input": "When did the movie The Matrix come out?"})
