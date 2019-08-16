# Nathan Cieminski Chatterbot Assignment 8/13/19

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
mybot = ChatBot("Friendly")
conversation = [
    "Hello, how are you doing today?",
    "Sup!",
    "What are you doing today?",
    "Tell me your name!"
    "I'm trying to think of something."
    "You can only be happy if you are happy with yourself."
    "I could be a lot better, but I'm working on it.",
    "I love talking to you",
    "You're Awesome",
    "Tell me about your day."
    "I'm so glad you can tell me anything.",
    "You will get better one day at a time, just be patient.",
    "Thank you.",
    "You're welcome."
    "What is your favorite football team?",
    "What do you do for a living?",
    "What is your favorite video game genre?",
    "Do you like cookies? I love cookies.",
    "Do you like scary movies?",
    "Do you have a favorite movie category?",
    "Who was your favorite Avenger?",
    "Are you a student or work all the time?",
    "What is your dream vacation?",
]
trainer = ListTrainer(mybot)
trainer.train(conversation)
print("Tell me what you want to talk about  ")
#add loop
while True:
    try:
        user_input = input()
        bot_response = mybot.get_response(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break