#Project 1 Simple Rule-Based Chatbot 

def chatbot():
    print("===================================")
    print("       Simple Rule-Based Chatbot")
    print("===================================")
    print("Bot: Hello! I am a simple chatbot.")
    print("Bot: Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How are you?")

        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I am doing great! Thanks for asking.")

        elif user_input in ["what is your name", "what's your name"]:
            print("Bot: My name is SimpleBot.")

        elif user_input in ["who are you", "what are you"]:
            print("Bot: I am a rule-based chatbot created using Python.")

        elif user_input in ["what can you do", "help"]:
            print("Bot: I can respond to greetings and some predefined questions.")

        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


chatbot()
