import re

# Define some predefined rules and responses
rules = {
    r'hello|hi|hey': 'Hello! How can I assist you today?',
    r'thanks': 'welcome!',
    r'how are you': 'I am fine. How about you?',
    r'what is your name': 'I am a Kalyan Singh. You can call me Kalyan.',
    r'What are you doing': 'I am a studying.',
    r'Which department': 'My department is BCA.',
    r'Where university': 'Galhotias University.',
    r'What have you done in the project': 'I have made a project of chatbot in which it respose but there are three of us in this project.',
    r'bye|goodbyhie': 'Goodbye! Have a great day!'
}

# Function to find a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    
    # Iterate through the rules and find a matching response
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    # If no match found, provide a default response
    return "I'm sorry, I didn't understand that."

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
