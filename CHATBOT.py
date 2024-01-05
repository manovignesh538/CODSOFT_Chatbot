import re

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define patterns and corresponding responses
    greetings_patterns = ["hi", "hello", "hey", "greetings"]
    farewell_patterns = ["bye", "goodbye", "see you", "farewell"]
    weather_patterns = ["weather", "temperature", "forecast"]
    default_response = "I'm sorry, I don't understand. Can you be more specific?"

    # Check for patterns and provide responses
    if any(pattern in user_input for pattern in greetings_patterns):
        return "Hello! How can I assist you today?"

    elif any(pattern in user_input for pattern in farewell_patterns):
        return "Goodbye! Have a great day."

    elif any(pattern in user_input for pattern in weather_patterns):
        return "I'm sorry, I don't have real-time weather information right now."

    else:
        return default_response

def main():
    print("Simple Rule-Based Chatbot: Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
