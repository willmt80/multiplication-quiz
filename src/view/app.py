from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer
import sys

from .start_menu import StartMenu
from .game_page import GamePage
from .answers_page import AnswersPage
from .view_helpers import get_new_game, get_equation_label

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle("Multiplication table")
        self.max = 9
        self.num_questions = 50
        self.init_ui()
    
    def init_ui(self):
        self.stacked_widget = QStackedWidget(self)
        self.start_menu = StartMenu()
        self.stacked_widget.addWidget(self.start_menu)
        self.stacked_widget.setCurrentIndex(0)
        self.setCentralWidget(self.stacked_widget)

        self.start_menu.start_button.clicked.connect(self.start_game)
        self.start_menu.max_slider.valueChanged.connect(self.set_max)
        self.start_menu.max_slider.setValue(self.max)
        self.start_menu.max_value.setText(str(self.max))

        self.start_menu.question_slider.valueChanged.connect(self.set_question_amount)
        self.start_menu.question_slider.setValue(self.num_questions // 10)
        self.start_menu.question_value.setText(str(self.num_questions))

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)

    def get_current_equation_label(self):
        return get_equation_label(self.game_state.get_cur_left(), self.game_state.get_cur_right())
    
    def get_current_question_count(self):
        return str(self.game_state.current + 1) + " / " + str(self.num_questions)
    
    def make_guess(self):
        self.game_state.make_guess(int(self.game_page.input.text()))
        if self.game_state.do_equations_remain():
            self.game_page.question_count.setText(self.get_current_question_count())
            self.game_page.label.setText(self.get_current_equation_label())
        else:
            self.answers_page = AnswersPage()
            self.stacked_widget.insertWidget(2, self.answers_page)
            self.answers_page.display_answers(self.game_state.answers, self.time)
            self.answers_page.return_button.clicked.connect(self.return_to_menu)
            self.stacked_widget.setCurrentIndex(2)
        self.game_page.input.setText("")

    
    def start_game(self):
        self.game_state = get_new_game(self.max, self.num_questions)
        self.game_page = GamePage()
        self.stacked_widget.insertWidget(1, self.game_page)
        self.game_page.button.clicked.connect(self.make_guess)
        self.game_page.question_count.setText(self.get_current_question_count())
        self.game_page.label.setText(self.get_current_equation_label())
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.game_page.time_label.setText(self.time.toString("mm:ss"))
        self.stacked_widget.setCurrentIndex(1)
    
    def set_max(self, value):
        self.max = value
        self.start_menu.max_value.setText(str(value))
        self.start_menu.max_value.adjustSize()

    def set_question_amount(self, value):
        self.num_questions = value * 10
        self.start_menu.question_value.setText(str(value * 10))
        self.start_menu.question_value.adjustSize()

    def timer_event(self):
        self.time = self.time.addSecs(1)
        self.game_page.time_label.setText(self.time.toString("mm:ss"))

    def return_to_menu(self):
        self.stacked_widget.setCurrentIndex(0)


def start_app():
    app = QApplication([])
    win = App()
    win.show()
    
    sys.exit(app.exec_())

