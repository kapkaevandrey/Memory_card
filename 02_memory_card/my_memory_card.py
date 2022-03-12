import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QPushButton, QLabel, QVBoxLayout,
                             QHBoxLayout, QGroupBox)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Memory Card")

# widgets
button_answer = QPushButton("Ответить")
question = QLabel("Какого цвета ёлка?")
answer_group_btn = QGroupBox("Варинаты ответов:")
btn_1 = QRadioButton("green")
btn_2 = QRadioButton("blue")
btn_3 = QRadioButton("yellow")
btn_4 = QRadioButton("WTF")

# line main window
main_line = QVBoxLayout()
line_up = QHBoxLayout()
line_mid = QHBoxLayout()
line_down = QHBoxLayout()

# add line in group box
left_group_line = QVBoxLayout()
right_group_line = QVBoxLayout()
line_horizon_group = QHBoxLayout()

left_group_line.addWidget(btn_1)
left_group_line.addWidget(btn_2)
right_group_line.addWidget(btn_3)
right_group_line.addWidget(btn_4)

line_horizon_group.addLayout(left_group_line)
line_horizon_group.addLayout(right_group_line)

# add group line in GROUP BOX
answer_group_btn.setLayout(line_horizon_group)

# final
line_up.addWidget(question)
line_mid.addWidget(answer_group_btn)
line_down.addWidget(button_answer)

main_line.addLayout(line_up)
main_line.addLayout(line_mid)
main_line.addLayout(line_down)

window.setLayout(main_line)

window.show()
app.exec()

