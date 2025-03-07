import tkinter as tk

def on_click():
    user_input = entry.get().strip()
    if user_input:
        chat_display.config(state=tk.NORMAL)
        #! Testing print(user_input)

        chat_display.insert(tk.END, "You: " + user_input + "\n")

        response_text = input("Chatbot response: ")

        chat_display.insert(tk.END, "Movie Chat Bot: " + response_text + "\n") #! Testing

        chat_display.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Movie Research Assistant")

chat_display = tk.Text(root, wrap="word", state=tk.DISABLED, bg="white", height=15, width=50)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

btn = tk.Button(root, text="Send", command=on_click)
btn.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()
