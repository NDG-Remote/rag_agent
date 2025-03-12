# Project Architecture

This document provides a brief overview of the main purpose of each `.py` file in the project.

## Files
### `main.py`
The main entry point of the application. It processes user input, extracts movie/TV series names, interacts with the AI agent, and updates the GUI with the results.

### `agent.py`
Handles the interaction with the AI model and external tools like IMDb and Google Search to provide answers to user queries about movies and TV series.

### `gui.py`
Defines the graphical user interface (GUI) using Tkinter. It includes functions for displaying messages, handling user input, and updating the GUI.

### `imdb_api.py`
Contains functions to interact with the IMDb API to fetch data about movies and TV series.

### `name_filter.py`
Includes functions to extract and format the name of a movie or TV series from a user's question using the OpenAI API.

### `youtube.py`
Contains functions to search for YouTube links, specifically for finding official trailers of movies and TV series.

### `config.py`
Currently empty. This file can be used to store configuration settings for the project.

### `utils.py`
Currently empty. This file can be used to store utility functions that are used across the project.
