from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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

        self.max_value = QLabel(self)
        self.max_value.setFont(QFont('Arial', 16))
        layout.addWidget(self.max_value)

        self.max_slider = QSlider(self)
        self.max_slider.setOrientation(Qt.Horizontal)
        self.max_slider.setTickInterval(1)
        self.max_slider.setMinimum(1)
        self.max_slider.setMaximum(20)
        self.max_slider.setTickPosition(QSlider.TicksBothSides)
        layout.addWidget(self.max_slider)

        self.question_label = QLabel(self)
        self.question_label.setText("Number of Questions:")
        self.question_label.adjustSize()
        self.question_label.setFont(QFont('Arial', 20))
        layout.addWidget(self.question_label)

        self.question_value = QLabel(self)
        self.question_value.setFont(QFont('Arial', 16))
        layout.addWidget(self.question_value)

        self.question_slider = QSlider(self)
        self.question_slider.setOrientation(Qt.Horizontal)
        self.question_slider.setTickInterval(1)
        self.question_slider.setMinimum(1)
        self.question_slider.setMaximum(10)
        self.question_slider.setTickPosition(QSlider.TicksBothSides)
        layout.addWidget(self.question_slider)

        self.start_button = QPushButton(self)
        self.start_button.setText("Start")
        layout.addWidget(self.start_button)
        self.setLayout(layout)