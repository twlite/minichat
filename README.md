# Minichat
Mini chatbot client based on AIML

# Installation

```sh
pip3 install minichat
```

# Example

```py
from minichat import minichat

chatbot = minichat.Minichat()

while True:
    question = input("You: ")
    answer = chatbot.chat(question)
    print("Bot:", answer)
```

## Created and maintained by SnowflakeDev Community ❄️