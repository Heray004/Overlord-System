import openai


class GPT:
    def __init__(self):
        openai.api_key = r"sk-xQBMS4G5hWNfe82jMGg-_KoFbrYYs"
        self.__messages = []

    def request(self, task):
        self.__messages.append({'role': 'user', 'content': task})
        print("Отправлено")
        answer = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=self.__messages

        )
        self.__messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content


if __name__ == '__main__':
    assist = GPT()
    data = input(">>> ")
    print(f"GPT answer: {assist.request(data)}")
