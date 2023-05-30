import os
import requests
import json


def chat_gpt3(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_KEY')}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    try:
        return response_json["choices"][0]["message"]["content"]
    except KeyError:
        print(f"Unexpected response: {response_json}")
        return ""


def main():
    while True:
        user_message = input("Enter your message (type 'exit' to quit): ")
        if user_message.strip().lower() == 'exit':
            break
        else:
            print("GPT-3 Response: ", chat_gpt3(user_message))


if __name__ == "__main__":
    main()
