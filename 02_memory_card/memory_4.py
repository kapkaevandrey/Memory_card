import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QRadioButton, QGroupBox,
                             QHBoxLayout, QVBoxLayout, QButtonGroup,
                             QMessageBox)

from question import User, Question


list_question = Question.generate_list_question()

user = User(num_of_quest=len(list_question))

q_start = Question("Готов начать?", "Да", "Нет", "Я ещё сплю", "Бегите глупцы")

# create app and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400, 400)

# add widgets
question = QLabel("Самый сложный вопрос")
result = QLabel("Верно/Не верно")
right_answer = QLabel("Правильный ответ")
btn_answer = QPushButton("Ответить")
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")
rbtn_group = QButtonGroup()
rbtn_group.addButton(rbtn_1)
rbtn_group.addButton(rbtn_2)
rbtn_group.addButton(rbtn_3)
rbtn_group.addButton(rbtn_4)
rbtn_group.variants = rbtn_group.buttons()
box_with_answers = QGroupBox("Варианты ответов")
box_with_result = QGroupBox("Результат теста")

# create lines and add widgets for box with answers variants
left_box_line = QVBoxLayout()
right_box_line = QVBoxLayout()
horizon_box_line = QHBoxLayout()
right_box_line.addWidget(rbtn_1, alignment=Qt.AlignCenter)
right_box_line.addWidget(rbtn_2, alignment=Qt.AlignCenter)
left_box_line.addWidget(rbtn_3, alignment=Qt.AlignCenter)
left_box_line.addWidget(rbtn_4, alignment=Qt.AlignCenter)
horizon_box_line.addLayout(right_box_line)
horizon_box_line.addLayout(left_box_line)
box_with_answers.setLayout(horizon_box_line)

# create lines and add widgets for box with result
box_result_line = QVBoxLayout()
box_result_line.addWidget(result, alignment=(Qt.AlignTop | Qt.AlignLeft))
box_result_line.addWidget(right_answer, alignment=Qt.AlignCenter, stretch=1)
box_with_result.setLayout(box_result_line)

# create lines for main window
up_line = QHBoxLayout()
mid_line = QHBoxLayout()
down_line = QHBoxLayout()
main_line = QVBoxLayout()

# add widgets to lines main window
up_line.addWidget(question)
mid_line.addWidget(box_with_answers)
mid_line.addWidget(box_with_result)
down_line.addStretch(1)
down_line.addWidget(btn_answer, stretch=2)
down_line.addStretch(1)

# add sub lines to main line
main_line.addLayout(up_line, stretch=2)
main_line.addLayout(mid_line, stretch=8)
main_line.addStretch(1)
main_line.addLayout(down_line, stretch=1)
main_line.addStretch(1)

window.setLayout(main_line)


################################################
# Functional                                   #
################################################
def push_button_answer_main():
    """Главная функция обработки события нажатия кнопки"""
    if box_with_result.isHidden() and is_buttons_check():
        box_with_answers.hide()
        check_answer()
        box_with_result.show()
        btn_answer.setText("Следующий вопрос")
        try_show_final_result()
    elif box_with_answers.isHidden() and len(list_question) != 0:
        box_with_result.hide()
        drop_answers_flags()
        task = get_question(list_question)
        set_question(task)
        box_with_answers.show()
        btn_answer.setText("Ответить")


def try_show_final_result():
    if len(list_question) != 0:
        return
    message = QMessageBox()
    message.setWindowTitle("Ваш результат")
    message.move(200, 200)
    message.resize(200, 200)
    message.setText(f"Ваш результат {user.counter} "
                    f"из {user.num_of_quest}")
    message.exec()





def get_question(questions: list):
    random.shuffle(questions)
    return questions.pop()

def is_buttons_check():
    return any([btn.isChecked() for btn in rbtn_group.buttons()])


def drop_answers_flags():
    rbtn_group.setExclusive(False)
    for btn in rbtn_group.buttons():
        btn.setChecked(False)
    rbtn_group.setExclusive(True)


def set_question(task: Question):
    question.setText(task.question)
    random.shuffle(rbtn_group.variants)
    rbtn_group.variants[0].setText(task.right_answer)
    rbtn_group.variants[1].setText(task.wrong1)
    rbtn_group.variants[2].setText(task.wrong2)
    rbtn_group.variants[3].setText(task.wrong3)


def check_answer():
    right_btn = rbtn_group.variants[0]
    if right_btn.isChecked():
        result.setText("Правильно")
        user.counter += 1
    else:
        result.setText("Не правильно")
    right_answer.setText(right_btn.text())


btn_answer.clicked.connect(push_button_answer_main)
################################################
# Run app                                      #
################################################
set_question(q_start)
box_with_result.hide()
window.show()
app.exec()