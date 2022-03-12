import json


class Question:
    def __init__(self, question: str, right_answer: str,
                 wrong1: str, wrong2: str, wrong3: str):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def __str__(self):
        return self.question

    def __repr__(self):
        return self.question


class User:
    def __init__(self, num_question: int):
        self.num_question = num_question
        self.counter = 0


with open(file="data.json", mode="r", encoding="utf8") as file:
    data = json.load(file)


list_question = []
for obj in data:
    q = Question(**obj)
    list_question.append(q)
