import logging
from gui import run_gui, on_click, set_on_click_callback, updating_chat_display, root
from agent import invoke_agent
from youtube import extract_youtube_link
from imdb_api import get_movie_series_name

# Configure logging
logging.basicConfig(filename="app.log", level=logging.ERROR,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def process_user_input(user_input):
    try:
        # Getting LLM answer from the Agent to the question
        agent_response = None
        try:
            updating_chat_display("Calling: Agent to answer your question", "calling_message")
            agent_response = invoke_agent(user_input)
            if not agent_response or agent_response == "":
                question_response = "I'm sorry, I couldn't find any information about the movie/TV series you asked for."
                updating_chat_display("Error: No answer from the model", "error_message")
                root.update()
            else:
                question_response = agent_response
                updating_chat_display("Result: " + question_response, "result_message")
                root.update()
        except Exception as e:
            question_response = f"An error occurred while searching for the answer: {str(e)}"
            logger.error(question_response)
            updating_chat_display(question_response, "error_message")
            root.update()

        # Extracting the YouTube link from the search result and updating the GUI
        movie_series_name = get_movie_series_name()
        if movie_series_name:
            youtube_link = None
            try:
                updating_chat_display("Calling: YouTube Search for the official trailer of \"" + movie_series_name + "\".", "calling_message")
                root.update()
                youtube_link = extract_youtube_link(movie_series_name).strip("[]'")
                if not youtube_link:
                    youtube_status_message = "Unfortunately, I couldn't find the official trailer on YouTube."
                    updating_chat_display("Result: No official movie trailer found on YouTube", "result_message")
                    root.update()
                else:
                    youtube_status_message = "Here's the YouTube link to the official trailer:"
                    updating_chat_display("Result: Found trailer: " + youtube_link, "result_message")
                    root.update()
            except Exception as e:
                youtube_status_message = f"An error occurred while searching for the YouTube link: {str(e)}"
                logger.error(youtube_status_message)
                updating_chat_display(youtube_status_message, "error_message")
                root.update()
        else:
            youtube_status_message = ""
            youtube_link = None

        # Writing final result, combining the LLM answer and the YouTube link
        final_response = f"FINAL ANSWER:\n\n{agent_response}\n\n{youtube_status_message}"

        # Sending final result to the GUI
        updating_chat_display(final_response, "final_result_message")
        if youtube_link:
            updating_chat_display(youtube_link, "link")
        root.update()
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logger.error(error_message)
        updating_chat_display(error_message, "error_message")
        root.update()

# Set up Python Tkinter GUI
set_on_click_callback(process_user_input)
run_gui()
