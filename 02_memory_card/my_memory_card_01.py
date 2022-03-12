import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QRadioButton, QGroupBox,
                             QHBoxLayout, QVBoxLayout, QButtonGroup)

from question_3 import Question, question_list

q1 = Question("Цвет ёлки", "Green", "Yellow", "Blue", "Gray")
q2 = Question("Готов начать", "Да", "Нет", "Нет", "нет")


# create app and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400, 300)

# create widgets buttons and labels for main window
button_answer_push = QPushButton("Ответить")
question_text = QLabel("Сложный вопрос")
ans_1 = QRadioButton("1")
ans_2 = QRadioButton("2")
ans_3 = QRadioButton("3")
ans_4 = QRadioButton("4")
rbtn_group = QButtonGroup()
rbtn_group.addButton(ans_1)
rbtn_group.addButton(ans_2)
rbtn_group.addButton(ans_3)
rbtn_group.addButton(ans_4)
rbtn_group.variants = rbtn_group.buttons() # [ans_1, ans_2, ans_3, ans_4]


# create group box question and group lines, add widgets to Box
box_with_answers = QGroupBox("Варианты ответов")
right_group_layout = QVBoxLayout()
left_group_layout = QVBoxLayout()
group_horizon_layout = QHBoxLayout()

left_group_layout.addWidget(ans_1, alignment=Qt.AlignCenter)
left_group_layout.addWidget(ans_2, alignment=Qt.AlignCenter)
right_group_layout.addWidget(ans_3, alignment=Qt.AlignCenter)
right_group_layout.addWidget(ans_4, alignment=Qt.AlignCenter)
group_horizon_layout.addLayout(left_group_layout)
group_horizon_layout.addLayout(right_group_layout)
box_with_answers.setLayout(group_horizon_layout)

# create group box result
box_with_result = QGroupBox("Результат теста")
result = QLabel("Верно/неверно")
correct_answer = QLabel("Correct answer")
answer_layout = QVBoxLayout()
answer_layout.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
answer_layout.addWidget(correct_answer, alignment=Qt.AlignCenter, stretch=1)
box_with_result.setLayout(answer_layout)

# create main lines and construct interface
main_line = QVBoxLayout()
up_line = QHBoxLayout()
mid_line = QHBoxLayout()
down_line = QHBoxLayout()

up_line.addWidget(question_text, alignment=Qt.AlignCenter)
mid_line.addWidget(box_with_answers)
mid_line.addWidget(box_with_result)
down_line.addStretch(1)
down_line.addWidget(button_answer_push, stretch=2)
down_line.addStretch(1)

main_line.addLayout(up_line, stretch=2)
main_line.addLayout(mid_line, stretch=8)
main_line.addStretch(1)
main_line.addLayout(down_line, stretch=1)
main_line.addStretch(1)

window.setLayout(main_line)


##################################################################
# Functional                                                     #
##################################################################
def push_button_main():
    if box_with_result.isHidden() and is_buttons_checked():
        box_with_answers.hide()
        check_answer()
        box_with_result.show()
        button_answer_push.setText("Следующий вопрос")
    elif box_with_answers.isHidden():
        box_with_result.hide()
        drop_flags()
        metter = get_question(question_list)
        set_question(metter)
        box_with_answers.show()
        button_answer_push.setText("Ответить")


def get_question(questions):
    if len(questions) == 0:
        return q2
    random.shuffle(questions)
    return questions.pop()


def is_buttons_checked():
    return any([btn.isChecked() for btn in rbtn_group.buttons()])


def check_answer():
    right_btn = rbtn_group.variants[0]
    if right_btn.isChecked():
        result.setText("Верно")
    else:
        result.setText("Не верно")
    correct_answer.setText(right_btn.text())


def set_question(task: Question):
    question_text.setText(task.question)
    random.shuffle(rbtn_group.variants)
    rbtn_group.variants[0].setText(task.right_answer)
    rbtn_group.variants[1].setText(task.wrong1)
    rbtn_group.variants[2].setText(task.wrong2)
    rbtn_group.variants[3].setText(task.wrong3)

def drop_flags():
    rbtn_group.setExclusive(False)
    for btn in rbtn_group.buttons():
        btn.setChecked(False)
    rbtn_group.setExclusive(True)


button_answer_push.clicked.connect(push_button_main)
##################################################################
# Run application                                                #
##################################################################
set_question(q2)
box_with_result.hide()
window.show()
app.exec()
