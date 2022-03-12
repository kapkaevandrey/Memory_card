import json
import random


class Question:
    def __init__(self, question, right_answer,
                 wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    @classmethod
    def generate_list_question(cls, path=""):
        with open(path + "data.json", mode="r", encoding="utf8") as file:
            data = json.load(file)
        list_question = [cls(**obj) for obj in data]
        return random.sample(list_question, 5)

class User:
    def __init__(self, questions_num: int):
        self.question_num = questions_num
        self.counter = 0
