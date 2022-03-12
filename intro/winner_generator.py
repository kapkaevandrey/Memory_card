import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout)


def generate_winner():
    num = random.randint(1, 99)
    winner_num.setNum(num)


# создаём приложение
app = QApplication(sys.argv)
# создаём главное окно
main_win = QWidget()
main_win.setWindowTitle("Определитель победителя!")
main_win.move(200, 200)
main_win.resize(400, 200)
main_win.show()
# создание элементов интерфейса
text = QLabel("Нажми чтобы узнать победителя!")
winner_num = QLabel("-")
button = QPushButton("Generate")
# привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner_num, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)
# обработка событий
button.clicked.connect(generate_winner)

# запуск приложения
app.exec_()
