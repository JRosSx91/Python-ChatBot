import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


def chat_gpt3(user_message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return completion.choices[0].message["content"]


def main():
    while True:
        user_message = input("Enter your message (type 'exit' to quit): ")
        if user_message.strip().lower() == 'exit':
            break
        else:
            print("GPT-3 Response: ", chat_gpt3(user_message))


if __name__ == "__main__":
    main()
