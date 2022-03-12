import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox)


def show_win():
    message = QMessageBox()
    message.setText("Верно!\nВы выиграли гироскутер")
    message.exec_()


# созадём приложение
app = QApplication(sys.argv)

# создаём главное окно
main_window = QWidget()
main_window.setWindowTitle("Конкурс от Crazy People")
main_window.resize(400, 200)
main_window.show()

# создаём виджеты
text = QLabel("В каком году канал получил \"золотую кнопку\" от YouTube?")
btn_1 = QRadioButton("2005")
btn_2 = QRadioButton("2010")
btn_3 = QRadioButton("2015")
btn_4 = QRadioButton("2020")

# создадим направляющие линии
main_line = QVBoxLayout()
up_line = QHBoxLayout()
mid_line = QHBoxLayout()
down_line = QHBoxLayout()

# присоединяем виджеты к нужным линиям
up_line.addWidget(text, alignment=Qt.AlignCenter)
mid_line.addWidget(btn_1, alignment=Qt.AlignCenter)
mid_line.addWidget(btn_2, alignment=Qt.AlignCenter)
down_line.addWidget(btn_3, alignment=Qt.AlignCenter)
down_line.addWidget(btn_4, alignment=Qt.AlignCenter)
main_line.addLayout(up_line)
main_line.addLayout(mid_line)
main_line.addLayout(down_line)

# обработока событий
btn_1.clicked.connect(show_win)

# присоединяем направляющую к главному окну
main_window.setLayout(main_line)
# запустить приложение
app.exec_()