from minichat.core import Chatbot
from datetime import datetime

class Minichat:
    __slots__ = ('name', 'gender', 'birth_year', 'botmaster', 'chatbot')
    
    def __init__(self, name: str = "Minichat", gender: str = "female", birth_year: int = 1995, botmaster: str = "SnowflakeDev Community"):
        """Instantiate Minichat"""

        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.botmaster = botmaster
        self.chatbot = Chatbot()

    def chat(self, message) -> str:
        """Returns a response from the chatbot. If encountered error, returns fallback response"""

        if not message or isinstance(message, str) is False:
            raise TypeError("Message must be a non-empty string")

        response = self.chatbot.get_response(message=str(message))
        response = response.replace("CHAT_BOT_NAME", self.name)
        response = response.replace("CHAT_BOT_GENDER", self.gender)
        response = response.replace("CHAT_BOT_AGE", str(self.get_age()))
        response = response.replace("CHAT_BOT_MASTER", self.botmaster)
        return response

    def get_age(self) -> int:
        """Returns the age of the chatbot"""

        return datetime.now().year - self.birth_year
