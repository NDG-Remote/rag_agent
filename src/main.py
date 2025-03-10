from gui import run_gui, on_click, set_on_click_callback, updating_chat_display
from agent import get_answer
from name_filter import extract_name
from youtube import extract_youtube_link

def process_user_input(user_input):
    # Extracting the movie/TV-Serie name from the user input
    name = extract_name(user_input)

    # Sending message to the GUI
    updating_chat_display('Calling Google Search for your Question about "' + name + '".')

    # getting answer from the AI to the question
    answer = get_answer(user_input)
    if not answer:
        question_response = ("I don't know")
        updating_chat_display('Result: No information found')
        #? print(question_response)
    else:
        question_response = answer
        updating_chat_display('Result: ' + question_response)
        #? print(question_response)

    # Sending message to the GUI
    updating_chat_display('Calling YouTube Search for the official trailer of "' + name + '".')

    # Extracting the youtube link from the search result
    youtube_link = extract_youtube_link(name)
    if not youtube_link:
        youtube_response = ("Unfortunately I couldn't find the official movie trailer on Youtube")
        updating_chat_display('Result: No official movie trailer found on Youtube')
        #? print(youtube_response)
    else:
        youtube_response =(f"Here's the YouTube link to the official trailer: {youtube_link}")
        updating_chat_display('Found trailer: ' + youtube_link)
        #? print(youtube_response)

    # Combining the answer and the youtube link
    final_response = (f"Here's the answer to your question about the movie/TV-Serie '{name}':\n\n{answer}\n\n{youtube_response}")

    # Sending message to the GUI
    updating_chat_display(final_response)


# Set up Python Tkinter GUI
set_on_click_callback(process_user_input)
run_gui()
