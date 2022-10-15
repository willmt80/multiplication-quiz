from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class StartMenu(QWidget):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.max_label = QLabel(self)
        self.max_label.setText("Largest Factor:")
        self.max_label.adjustSize()
        self.max_label.setFont(QFont('Arial', 20))
        layout.addWidget(self.max_label)
        max_group=QButtonGroup(self)
        self.nine_button = QRadioButton("9")
        self.nine_button.max = 9
        self.nine_button.setFont(QFont('Arial', 20))
        max_group.addButton(self.nine_button)
        layout.addWidget(self.nine_button)
        self.twelve_button = QRadioButton("12")
        self.twelve_button.max = 12
        self.twelve_button.setFont(QFont('Arial', 20))
        max_group.addButton(self.twelve_button)
        layout.addWidget(self.twelve_button)

        self.question_label = QLabel(self)
        self.question_label.setText("Number of Questions:")
        self.question_label.adjustSize()
        self.question_label.setFont(QFont('Arial', 20))
        layout.addWidget(self.question_label)
        question_group=QButtonGroup(self)
        self.short_quiz_button = QRadioButton("25")
        self.short_quiz_button.num = 25
        self.short_quiz_button.setFont(QFont('Arial', 20))
        question_group.addButton(self.short_quiz_button)
        layout.addWidget(self.short_quiz_button)
        self.mid_quiz_button = QRadioButton("50")
        self.mid_quiz_button.num = 50
        self.mid_quiz_button.setFont(QFont('Arial', 20))
        question_group.addButton(self.mid_quiz_button)
        layout.addWidget(self.mid_quiz_button)
        self.long_quiz_button = QRadioButton("100")
        self.long_quiz_button.num = 100
        self.long_quiz_button.setFont(QFont('Arial', 20))
        question_group.addButton(self.long_quiz_button)
        layout.addWidget(self.long_quiz_button)

        self.start_button = QPushButton(self)
        self.start_button.setText("Start")
        layout.addWidget(self.start_button)
        self.setLayout(layout)