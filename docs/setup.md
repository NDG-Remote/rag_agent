# Project Setup

This document provides instructions for setting up the project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```
OPENAI_API_KEY = <your_openai_api_key>
RAPID_API_KEY = <your_openai_api_key>
GOOGLE_API_KEY = <your_openai_api_key>
GOOGLE_CSE_ID = <your_openai_api_key>
```

## Running the Application

1. **Start the application:**
    ```sh
    python src/main.py
    ```

2. **Interact with the GUI:**
    - Enter your question about a movie or TV series in the input field.
    - Click the "Send" button or press Enter to submit your question.
    - The application will display the results in the chat display area.

3. **Close the application:**
    - Use `Ctrl+C` in the terminal or the close button of the GUI.

## Additional Information

- **Logging:**
  - Logs are stored in the `app.log` file in the root directory.
  - Logging level is set to `ERROR` by default.

- **Configuration:**
  - The agent is set to `verbose=True`. This gives the possibility to see detailed logs of the agent's actions and decisions. If you prefer a cleaner output, you can set `verbose=False`.
  - Configuration settings can be added to the `config.py` file.
  - Utility functions can be added to the `utils.py` file.
