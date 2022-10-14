from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, Qt

class GamePage(QWidget):
    def __init__(self):
        super(GamePage, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel(self)
        self.label.move(120, 100)

        self.button = QPushButton(self)
        self.button.setText("Submit Answer")
        self.button.move(80, 160)
        self.button.setDisabled(True)

        validator = QRegExpValidator(QRegExp(r'[0-9]+'))

        self.input = QLineEdit(self)
        self.input.setValidator(validator)
        self.input.move(80, 130)
        self.input.setFocus()
        self.input.textChanged.connect(self.disable_button)

    def disable_button(self):
        if len(self.input.text()) > 0:
            self.button.setDisabled(False)
        else:
            self.button.setDisabled(True)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.button.click()