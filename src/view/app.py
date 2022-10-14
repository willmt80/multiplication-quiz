from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, Qt
from model.classes.game_state import GameState
from model.helpers import create_times_table, get_equation_list
import sys

from view.start_menu import StartMenu
from view.game_page import GamePage

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Multiplication table")
        self.init_ui()
    
    def init_ui(self):
        self.stacked_widget = QStackedWidget(self)
        self.start_menu = StartMenu()
        self.game_page = GamePage()
        self.stacked_widget.addWidget(self.start_menu)
        self.stacked_widget.addWidget(self.game_page)
        self.stacked_widget.setCurrentIndex(0)
        self.setCentralWidget(self.stacked_widget)

        self.start_menu.start_button.clicked.connect(self.start_game)

    def get_current_equation_label(self):
        return get_equation_label(self.game_state.get_cur_left(), self.game_state.get_cur_right())
    
    def make_guess(self):
        self.game_state.make_guess(self.game_page.input.text())
        self.game_page.label.setText(self.get_current_equation_label())
        self.game_page.input.setText("")
    
    def start_game(self):
        self.game_state = get_new_game(9, 20)
        self.game_page.button.clicked.connect(self.make_guess)
        self.game_page.label.setText(self.get_current_equation_label())
        self.stacked_widget.setCurrentIndex(1)

def get_new_game(max: int, count: int):
    times_table = create_times_table(max)
    return GameState(get_equation_list(times_table, count))

def get_equation_label(left: int, right: int):
    return str(left) + "x" + str(right)

def start_app():
    app = QApplication([])
    win = App()
    win.show()
    
    sys.exit(app.exec_())

