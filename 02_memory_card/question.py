import json


class Question:
    def __init__(self, question, right_answer,
                 wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    @classmethod
    def generate_list_question(cls, path="", file="data1.json", limit_num=0):
        with open(file=path + file, mode="r", encoding="utf8") as file:
            data = json.load(file)
        list_question = [cls(**q) for q in data]
        if limit_num > 0:
            return list_question[:limit_num]
        return list_question


class User:
    def __init__(self, num_of_quest: int):
        self.num_of_quest = num_of_quest
        self.counter = 0
