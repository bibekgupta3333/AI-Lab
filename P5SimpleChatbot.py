# Define the chat bot's rules
rules = {
    "hi": "Hello, how can I assist you today?",
    "bye": "Goodbye!",
    "what is your name": "My name is Chat Bot.",
    "what is the weather like today": "I'm sorry, I am not capable of providing weather information at this moment.",
    "what is the time": "The current time is XX:XX",
    "how are you": "I'm doing well, thank you for asking."
}
# Define the chat bot function
def chat_bot():
    # Print a greeting message
    print("Hello, I'm a chat bot. How can I assist you today?")

    # Keep the chat bot running
    while True:
        # Get user input
        user_input = input().lower()

        # Check if the user wants to exit
        if user_input == "bye":
            print(rules["bye"])
            break

        # Check if the user input matches any of the rules
        if user_input in rules:
            print(rules[user_input])
        else:
            print("I'm sorry, I don't understand. Please try again.")
# Test the chat bot
chat_bot()
