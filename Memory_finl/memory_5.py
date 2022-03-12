import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QGroupBox, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QButtonGroup,
                             QMessageBox)

from question import User, Question

list_question = Question.generate_list_question()
user = User(questions_num=len(list_question))

# create application and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Memory Card")

# create widgets for main window
question = QLabel("Сложный вопрос")
test_result = QLabel("Верно/Неверно")
right_answer = QLabel("Правильный ответ")
btn_answer = QPushButton("Ответить")
box_with_result = QGroupBox("Результат теста")
box_with_answers = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")
radio_group = QButtonGroup()  # создаём группу кнопок
radio_group.addButton(rbtn_1) # добавляем кнопки в группу
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)
radio_group.answers = radio_group.buttons()

# create lines for box with variants of answers
right_group_line = QVBoxLayout()
left_group_line = QVBoxLayout()
central_h_line = QHBoxLayout()

right_group_line.addWidget(rbtn_1, alignment=Qt.AlignCenter)
right_group_line.addWidget(rbtn_2, alignment=Qt.AlignCenter)
left_group_line.addWidget(rbtn_3, alignment=Qt.AlignCenter)
left_group_line.addWidget(rbtn_4, alignment=Qt.AlignCenter)
central_h_line.addLayout(right_group_line)
central_h_line.addLayout(left_group_line)
box_with_answers.setLayout(central_h_line)

# create lines and made box
vertical_box_line = QVBoxLayout()
vertical_box_line.addWidget(test_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
vertical_box_line.addWidget(right_answer, alignment=Qt.AlignHCenter, stretch=1)
box_with_result.setLayout(vertical_box_line)

# create lines for main window
main_line = QVBoxLayout()
up_line = QHBoxLayout()
mid_line = QHBoxLayout()
down_line = QHBoxLayout()

# add widgets to layout
up_line.addWidget(question)
mid_line.addWidget(box_with_answers)
mid_line.addWidget(box_with_result)
down_line.addStretch(1)
down_line.addWidget(btn_answer, stretch=2)
down_line.addStretch(1)

main_line.addLayout(up_line, stretch=2)
main_line.addLayout(mid_line, stretch=8)
main_line.addStretch(1)
main_line.addLayout(down_line, stretch=1)
main_line.addStretch(1)

window.setLayout(main_line)


###########################################################
# Functional                                              #
###########################################################

def is_checked():
    return any([btn.isChecked() for btn in radio_group.buttons()])


def start_test():
    if box_with_result.isHidden() and is_checked():
        box_with_answers.hide()
        check_answer()
        box_with_result.show()
        btn_answer.setText("Следующий вопрос")
    elif box_with_answers.isHidden() and len(list_question) != 0:
        box_with_result.hide()
        drop_flags()
        metter = chose_question(list_question)
        set_question(metter)
        box_with_answers.show()
        btn_answer.setText("Ответить")
    elif len(list_question) == 0:
        show_result()

def chose_question(question_list: list):
    random.shuffle(question_list)
    return question_list.pop()

def drop_flags():
    radio_group.setExclusive(False)
    for btn in radio_group.buttons():
        btn.setChecked(False)
    radio_group.setExclusive(True)


def set_question(metter: Question):
    question.setText(metter.question)
    random.shuffle(radio_group.answers)
    radio_group.answers[0].setText(metter.right_answer)
    radio_group.answers[1].setText(metter.wrong1)
    radio_group.answers[2].setText(metter.wrong2)
    radio_group.answers[3].setText(metter.wrong3)


def check_answer():
    right = radio_group.answers[0].text()
    if radio_group.answers[0].isChecked():
        test_result.setText("Правильно")
        user.counter += 1
    else:
        test_result.setText("Не правильно")
    right_answer.setText(right)


def show_result():
    message = QMessageBox()
    message.resize(200, 200)
    message.move(100, 100)
    message.setWindowTitle("Результаты теста")
    message.setText(f"Ваш результат {user.counter} из {user.question_num}.")
    message.exec()


btn_answer.clicked.connect(start_test)
###########################################################
#   Run application                                       #
###########################################################
q_test = Question("1", "2", "3", "4", "5")
set_question(q_test)
box_with_result.hide()
window.show()
app.exec()
