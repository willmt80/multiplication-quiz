from PyQt5.QtWidgets import *
from model.classes.answer import Answer
from view.view_helpers import get_answer_label

class AnswersPage(QWidget):
    def __init__(self):
        super(AnswersPage, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        self.list_layout = QGridLayout()

        self.setLayout(self.list_layout)

    def display_answers(self, answers: list[Answer]):
        for i, answer in enumerate(answers):
            label = QLabel(self)
            if (answer.get_correct_answer() == answer.guess):
                label.setText(str(i+1) + ". " + get_answer_label(answer, False))
            else:
                label.setText(str(i+1) + ". " + get_answer_label(answer, True))
                label.setStyleSheet("color: red")
            
            self.list_layout.addWidget((label), i // 3, i % 3)