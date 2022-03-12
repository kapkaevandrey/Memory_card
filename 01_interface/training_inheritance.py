class Widget:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def get_info(self):
        print(f"Надпись: {self.text}")
        print(f"Расположение: {self.x}, {self.y}")


class Button(Widget):
    def __init__(self, text, x, y, is_clicked: bool):
        super().__init__(text, x, y)
        self.is_clicked = is_clicked
    # дополненные свойства класса (в конструкторе)

    def click(self):
        self.is_clicked = True
        print("Вы зарегистрированы")

    # новые методы

# создай экземпляр класса Button
# если на вопрос «Хотите зарегистрироваться?» пользователь ответил «да», то примените метод click
button = Button(text="Участвовать", x=100, y=100, is_clicked=False)
button.get_info()
answer = input("Do you want sign up? >>> ")
if answer == "yes":
    button.click()

