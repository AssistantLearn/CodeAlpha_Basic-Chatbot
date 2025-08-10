def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("Chatbot: Hi there! How can I help you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a chatbot with no name. But you can name me!")
        elif "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()