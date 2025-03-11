import tkinter as tk

callback_function = None

def set_on_click_callback(callback):
    global callback_function
    callback_function = callback

def on_click():
    user_input = entry.get().strip()
    if user_input:
        chat_display.config(state=tk.NORMAL)

        chat_display.insert(tk.END, "\n" + user_input + "\n\n", "user_message")
        chat_display.insert(tk.END, "\n", "empty_message")

        chat_display.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        if callback_function:
            callback_function(user_input)

def updating_chat_display(response_text, message_type="empty_message"):
    chat_display.config(state=tk.NORMAL)

    chat_display.insert(tk.END, "\n" + response_text + "\n\n", message_type)
    chat_display.insert(tk.END, "\n", "empty_message")

    chat_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("AI Movie Research Assistant")

chat_display = tk.Text(root, wrap="word", state=tk.DISABLED, bg="white", height=15, width=50)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Define message styles
chat_display.tag_configure("user_message", foreground="black", background="#90EE90")  # Light green for user
chat_display.tag_configure("result_message", foreground="black", background="#ADD8E6")  # Light blue for bot results
chat_display.tag_configure("calling_message", foreground="black", background="#FFFFE0")  # Light yellow for calling messages
chat_display.tag_configure("final_result_message", foreground="black", background="#D3D3D3")  # Light grey for final result messages
chat_display.tag_configure("empty_message", foreground="black", background="white")  # White for default messages


entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

btn = tk.Button(root, text="Send", command=on_click)
btn.grid(row=1, column=1, padx=10, pady=10)

def run_gui():
    root.mainloop()
