from PyQt5.QtWidgets import *

class StartMenu(QWidget):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.start_button = QPushButton(self)
        self.start_button.setText("Start")
        self.start_button.move(80, 160)