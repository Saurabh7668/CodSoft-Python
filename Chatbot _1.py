import tkinter as tk

def send_message():
    user_input = user_entry.get()
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)  # Clear the user input field
    # Call the chatbot function and get the response
    response = chatbot_response(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n")

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create and configure chat history text area
chat_history = tk.Text(root, height=10, width=40)
chat_history.pack()

# Create and configure user input entry field
user_entry = tk.Entry(root, width=40)
user_entry.pack()

# Create and configure send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()

def chatbot_response(user_input):
    # Predefined rules for responses
    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a computer program, so I don't have feelings, but I'm here to assist you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand that."

# Main program loop
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Chatbot")
    chat_history = tk.Text(root, height=10, width=40)
    chat_history.pack()
    user_entry = tk.Entry(root, width=40)
    user_entry.pack()
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()
    root.mainloop()
