from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime
from PyQt5.QtGui import QFont
from src.model.classes.answer import Answer
from .view_helpers import get_answer_label

class AnswersPage(QWidget):
    def __init__(self):
        super(AnswersPage, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        self.list_layout = QGridLayout()

        self.time_label = QLabel(self)
        self.time_label.setFont(QFont('Arial', 16))
        self.list_layout.addWidget(self.time_label, 0, 0)

        self.return_button = QPushButton(self)
        self.return_button.setText("Main Menu")
        self.list_layout.addWidget(self.return_button, 0, 3)

        self.setLayout(self.list_layout)

    def display_answers(self, answers: list[Answer], time: QTime):
        time_copy = time
        for i, answer in enumerate(answers):
            label = QLabel(self)
            if (answer.get_correct_answer() == answer.guess):
                label.setText(str(i+1) + ". " + get_answer_label(answer, False))
            else:
                label.setText(str(i+1) + ". " + get_answer_label(answer, True))
                label.setStyleSheet("color: red")
                time_copy = time_copy.addSecs(15)
            
            self.list_layout.addWidget((label), (i // 4) + 1, i % 4)

        self.time_label.setText("Time: " + time_copy.toString("mm:ss"))
            