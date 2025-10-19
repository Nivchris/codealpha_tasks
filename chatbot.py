def chatbot():
    print(" Hello! I'm ChatBot. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower() 

        if user_input == "hello":
            print("Bot: Hi there! ")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user_input == "i am fine" or user_input == "i'm fine":
            print("Bot: Glad to hear that! ")
        elif user_input == "what is your name":
            print("Bot: I'm your friendly internship chatbot ")
        elif user_input == "bye":
            print("Bot: Goodbye!  Have a great day!")
            break
        else:
            print("Bot: Sorry, I didn't understand that. ")
chatbot()
