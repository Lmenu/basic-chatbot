import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm just a computer program, but I'm functioning well. How can I assist you today?"]],
    ["what's your name?", ["I'm just a chatbot, so I don't have a name. How can I help you?"]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!"]],
    ["Are you AI?", ["No, I am a chatbot!", "No!"]],
    # add more like this .
    
    
]
#simple code
chatbot = Chat(pairs, reflections)

def main():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    main()




