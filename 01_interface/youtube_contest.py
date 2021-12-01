import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox)


def show_win():
    message = QMessageBox(text="You are winner!")
    message.setWindowTitle("Winner")
    message.exec()


def show_lose():
    message = QMessageBox(text="You are loser!")
    message.setWindowTitle("Sorry")
    message.exec()


# create app and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Конкурс от Crazy People")
window.resize(400, 200)

# add widgets
question = QLabel('В каком году канал получил "золотую кнопку" на Youtube')
btn_1 = QRadioButton("2005")
btn_2 = QRadioButton("2010")
btn_3 = QRadioButton("2015")
btn_4 = QRadioButton("2020")

# add lines
main_line = QVBoxLayout()
up_line = QHBoxLayout()
mid_line = QHBoxLayout()
down_line = QHBoxLayout()

# add widgets to horizon lines
up_line.addWidget(question, alignment=Qt.AlignCenter)
mid_line.addWidget(btn_1, alignment=Qt.AlignCenter)
mid_line.addWidget(btn_2, alignment=Qt.AlignCenter)
down_line.addWidget(btn_3, alignment=Qt.AlignCenter)
down_line.addWidget(btn_4, alignment=Qt.AlignCenter)

main_line.addLayout(up_line)
main_line.addLayout(mid_line)
main_line.addLayout(down_line)
window.setLayout(main_line)

# connect ro event
btn_1.clicked.connect(show_lose)
btn_2.clicked.connect(show_lose)
btn_3.clicked.connect(show_win)
btn_4.clicked.connect(show_lose)

# run app
window.show()
app.exec()
