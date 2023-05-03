from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup, QVBoxLayout
from random import shuffle, randint
app = QApplication([])
btn_ok = QPushButton('Ответить')
lb_question = QLabel('Самый сложный вопрос в мире!')


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России', 'зеленый', 'синий', 'красный', 'белый'))
question_list.append(Question('Национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))
question_list.append(Question('Столица Канады', 'Оттава', 'Осло', 'Копенгаген', 'Хельсинки'))
question_list.append(Question('Национальная одежда Японии', 'кимоно', 'ханьфу', 'ханбок ', 'юпа'))
question_list.append(Question('Какая страна на 3 месте по площади в мире', 'Китай', 'Россия', 'Бразилия', 'США'))



RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment= (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Стастистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Стастистика\n-Всего вопросов:', window.total, '\n-Правильых ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()
