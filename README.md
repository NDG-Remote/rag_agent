# RAG Agent

## Overview

The RAG Agent is a Tkinter-based GUI application that allows users to ask questions about movies and TV series. The AI behind the chat not only uses its training data but also fetches additional information from IMDB and Google Search. Additionally, it provides a YouTube link to the official trailer.

## Core Functionality

- **Chat Box GUI:** Users can ask questions about movies and TV series.
- **AI Responses:** The AI answers questions using its training data and additional data fetched from IMDB and Google Search.
- **YouTube Links:** Provides links to official trailers.

## RAG Functionality

- **Reliable Data:** The LLM uses reliable data from the IMDB database.
- **Google Search:** For very current questions or those not covered by training data, the LLM performs a Google search.

## Tools and Technologies

- **LangChain:** Utilizes the LangChain framework.
- **Google Search Tool:** [Google Search Integration](https://python.langchain.com/docs/integrations/tools/google_search/)
- **YouTube Search Tool** [YouTube Integration](https://python.langchain.com/docs/integrations/tools/youtube/)
- **IMDB API:** Accessed through RapidAPI.
- **LLM:** ChatGPT
- **Custom Prompts:** Self-written prompts for specific queries.

## Getting Started

For setup instructions, refer to the [setup.md](../main/docs/setup.md) file.