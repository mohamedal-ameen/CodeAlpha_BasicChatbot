def chatbot():

    print("🤖 Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")

        elif user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: I'm a simple Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created as part of the CodeAlpha Python Internship.")

        elif user == "help":
            print("Bot: You can say hello, hi, how are you, or ask my name.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()