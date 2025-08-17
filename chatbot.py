from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot("SimpleBot")
trainer = ChatterBotCorpusTrainer(chatbot)

# Train with English dataset
trainer.train("chatterbot.corpus.english")

# Chat loop
print("🤖 Chatbot ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
