import aiml
import os
import pkg_resources
import random

class Chatbot:
    STARTUP_FILE = "startup.xml"

    def __init__(self) -> None:
        self.random_response = [
            "Sorry, I can't understand",
            "Can you say that again?",
            "What do you mean?",
            "Hmm",
            "I don't know D:",
            "D:",
            "What?",
            "*thinks*"
        ]

        self.aiml_kernel = aiml.Kernel()
        self.setup_aiml()

    def setup_aiml(self) -> None:
        initial_dir = os.getcwd()
        os.chdir(pkg_resources.resource_filename(__name__, ''))

        # Set default values
        self.aiml_kernel.setBotPredicate("name", "CHAT_BOT_NAME")
        self.aiml_kernel.setBotPredicate("gender", "CHAT_BOT_GENDER")
        self.aiml_kernel.setBotPredicate("age", "CHAT_BOT_AGE")
        self.aiml_kernel.setBotPredicate("master", "CHAT_BOT_MASTER")

        # Load AIML
        self.aiml_kernel.learn(self.STARTUP_FILE)
        self.aiml_kernel.respond("LOAD AIML A")
        self.aiml_kernel.respond("LOAD AIML B")
        os.chdir(initial_dir)

    def get_response(self, message) -> str:
        if not message: return random.choice(self.random_response)

        try:
            response = self.aiml_kernel.respond(message)
            if not response or len(response) < 1: return random.choice(self.random_response)
            return response
            
        except Exception as e:
            return random.choice(self.random_response)
