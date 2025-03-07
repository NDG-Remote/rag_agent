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

# Set up the agent

# Set up Python Tkinter GUI

# Set up all necessary API Keys and other base stuff

# Takeing user input from GUI and save it in a string variable

### Getting basic information from the user input with AI ###
# Asking LLM to filter out the movie/TV-Serie name from the question, (improve orthography if necessary) and save it in a string variable
# Asking LLM to filter out if it is a movie or a TV-Serie and save it in a string variable

### Getting Google Search Tool information ###
#! Sending Terminal Output "Calling Google Search: ... " to GUI
# Sending the movie/TV-Serie name to Google Search with site:imdb.com
#! If - search result is empty, send message to GUI "I don't know"
# Else - Taking first search result and save it in a string variable

# Sending Search Result (IMDB) URL to AI and get the movie/TV-Serie information
#! Sending Terminal Output "Result:  ... " to GUI

### Getting YouTube trailer ###
# sending movie/TV-serie name +  "oficial trailer" with LangChain YouTube Tool
#! Sending Terminal Output "Calling YouTube Search: ... " to GUI
# If - search result is empty, message = "Unforunately I couldn't find the oficial movie trailer on Youtube"
# Else - Taking first search result and save it in a string variable f"Here's the oficial movie trailer: {youtube_url}"

### Creating the final response ###
# Concatenating all the information (first + second part) in a string variable

#! Sending Result Message to GUI

# Setting everything to 0 for next question.
