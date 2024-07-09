# chatbot.py

class Chatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey"]
        self.farewells = ["bye", "exit", "goodbye"]
        self.name = "Chatbot"

    def respond(self, user_input):
        user_input = user_input.strip().lower()
        
        if any(greet in user_input for greet in self.greetings):
            return "Hello! How can I assist you?"
        elif "how are you" in user_input:
            return " I'm doing well! How about you?"
        elif "your name" in user_input:
            return f"I am {self.name},you can call me sofia ,i'm created to assist you."
        elif any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that."

    

    def start(self):
        print("Hello! I am a simple chatbot. How can I help you today?")
        while True:
            try:
                user_input = input("You: ")
                if user_input.strip() == "":
                    raise ValueError("Input cannot be empty. Please say something.")
                response = self.respond(user_input)
                print(f"Bot: {response}")
                if any(farewell in user_input for farewell in self.farewells):
                    break
            except ValueError as e:
                print(f"Bot: {e}")
            except Exception as e:
                print(f"Bot: An unexpected error occurred: {e}")
