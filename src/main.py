import logging
from gui import run_gui, on_click, set_on_click_callback, updating_chat_display, root
from agent import invoke_agent
from name_filter import extract_name
from youtube import extract_youtube_link

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_user_input(user_input):
    try:
        # Extracting the movie/TV-Serie name from the user input
        name = None
        try:
            updating_chat_display("Calling Name Extraction for the movie/TV-Serie.", "calling_message")
            name = extract_name(user_input).strip()
            invalid_names = ["", "''", '""']
            if name in invalid_names:
                name = None
        except Exception as e:
            error_message = f"An error occurred while extracting the movie/TV-Serie name: {str(e)}"
            logger.error(error_message)
            updating_chat_display(error_message, "error_message")
            root.update()

        # Getting the title response and updating the GUI
        if name:
            title_response = f"Here's the answer to your question about the movie/TV-Serie '{name}':\n\n"
            try:
                updating_chat_display('Result: Movie/TV-Serie is "' + name + '".', "result_message")
                root.update()
            except Exception as e:
                error_message = f"An error occurred while updating the display for showing the movie/TV-Serie: {str(e)}"
                logger.error(error_message)
                updating_chat_display(error_message, "error_message")
                root.update()
        else:
            title_response = ""


        # Getting answer from the AI to the question
        try:
            updating_chat_display("Calling: LLM for answer", "calling_message")
            answer = invoke_agent(user_input)
            if not answer:
                question_response = ("I'm sorry, I couldn't find any information about the movie/TV-Serie you asked for.")
                updating_chat_display("Result: No information found", "result_message")
                root.update()
            else:
                if name:
                    question_response = answer
                    updating_chat_display('Result: ' + question_response, "result_message")
                    root.update()
        except Exception as e:
            question_response = f"An error occurred while searching for the answer: {str(e)}"
            logger.error(question_response)
            updating_chat_display(question_response, "error_message")
            root.update()


        # Extracting the youtube link from the search result and updating the GUI
        if name:
            try:
                updating_chat_display('Calling YouTube Search for the official trailer of "' + name + '".', "calling_message")
                root.update()
                youtube_link = extract_youtube_link(name)
                if not youtube_link:
                    youtube_response = ("Unfortunately I couldn't find the official trailer on Youtube")
                    updating_chat_display('Result: No official movie trailer found on Youtube', "result_message")
                    root.update()
                else:
                    youtube_response =(f"Here's the YouTube link to the official trailer: {youtube_link}")
                    updating_chat_display("Result: Found trailer: " + youtube_link, "result_message")
                    root.update()
            except Exception as e:
                youtube_response = f"An error occurred while searching for the YouTube link: {str(e)}"
                logger.error(youtube_response)
                updating_chat_display(youtube_response, "error_message")
                root.update()
        else:
            youtube_response = ""

        # Combining the answer and the YouTube link
        final_response = (f"{title_response}{answer}\n\n{youtube_response}\n")

        # Sending message to the GUI
        updating_chat_display(final_response, "final_result_message")
        root.update()
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logger.error(error_message)
        updating_chat_display(error_message, "error_message")
        root.update()

# Set up Python Tkinter GUI
set_on_click_callback(process_user_input)
run_gui()
