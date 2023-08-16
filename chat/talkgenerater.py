import openai
import json

class TalkGenerator:

    def start(self, topic):
        messages = [
            {
                "role": "user",
                "content": '''Can you write me five questions related to being in the ''' + topic + '''}?

                            Please answer in JSON format
                            Here is the example of answer:
                            {
                                "q1" : "What kind of movie do you want to watch?",
                                "q2": "Oh, I like Tom Hardy, do you like him?",
                                "q3": "Do you want to eat some popcorn?",
                                "q4": "How was the movie?",
                                "q5": "Do you like comedy?"
                            }
                            '''
            }
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        questions_dict = json.loads(completion["choices"][0]["message"]["content"])
        questions_list = [questions_dict[f'q{i}'] for i in range(1, 6)]
        return questions_list

    # I usually ate pizza but today I want to eat hamburger
    def reply(self, ans):
        messages = [
            {
                "role": "user",
                "content": ans + "\n" +
                           '''
                            If my sentence has any grammatical errors, please correct them.

                            Please answer in JSON format
                            Here is the example of answer:
                            {
                                "answer" : "I used to eat pizza frequently, but today I'm craving a hamburger."
                            }
                            '''
            }
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        print(completion)
        reply = json.loads(completion["choices"][0]["message"]["content"])
