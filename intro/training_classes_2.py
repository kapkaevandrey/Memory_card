class Title():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.visual = True

    def get_info(self):
        print("Кнопка:", self.text)
        print(f"Расположение: {(self.x, self.y)}")
        print(f"Видимость:, {self.visual}")

    def show(self):
        self.visual = True
        print(f"{self.text} - отображается")

    def hide(self):
        self.visual = False
        print(f"{self.text} - скрыто")

    #конструктор

    #методы

#создай две надписи

#скрой вторую надпись