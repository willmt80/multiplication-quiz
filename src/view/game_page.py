from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtCore import QRegExp, Qt

class GamePage(QWidget):
    def __init__(self):
        super(GamePage, self).__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.question_count = QLabel(self)
        self.question_count.setFont(QFont('Arial', 20))
        layout.addWidget(self.question_count)

        self.time_label = QLabel(self)
        self.time_label.setFont(QFont('Arial', 30))
        layout.addWidget(self.time_label)

        self.label = QLabel(self)
        self.label.setFont(QFont('Arial', 40))
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        validator = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.input = QLineEdit(self)
        self.input.setMaxLength(3)
        self.input.setValidator(validator)
        self.input.setFocus()
        self.input.textChanged.connect(self.disable_button)
        self.input.setFont(QFont('Arial', 20))
        layout.addWidget(self.input)

        self.button = QPushButton(self)
        self.button.setText("Submit Answer")
        self.button.setDisabled(True)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def disable_button(self):
        if len(self.input.text()) > 0:
            self.button.setDisabled(False)
        else:
            self.button.setDisabled(True)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.button.click()