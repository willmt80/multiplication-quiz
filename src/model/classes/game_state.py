from .equation import Equation
from .answer import Answer

class GameState:
    def __init__(self, equation_list: list[Equation]):
        self.equation_list: list[Equation] = equation_list
        self.count: int = len(equation_list)
        self.current: int = 0
        self.answers: list[Answer] = []

    def get_current_equation(self):
        if self.current >= self.count:
            raise Exception("All equations have been answered")
        return self.equation_list[self.current]

    def make_guess(self, guess: int):
        if self.current >= self.count:
            raise Exception("All equations have been answered")
        current_equation = self.equation_list[self.current]
        self.answers.append(Answer(current_equation.left, current_equation.right, guess))
        self.current += 1

    def do_equations_remain(self):
        return self.current < self.count

    def get_cur_left(self):
        if self.current >= len(self.equation_list):
            raise Exception("All equations have been answered")
        return self.equation_list[self.current].left

    def get_cur_right(self):
        if self.current >= len(self.equation_list):
            raise Exception("All equations have been answered")
        return self.equation_list[self.current].right

    def get_answer_left(self, index):
        if index >= len(self.answers):
            raise Exception("Given index is out of bounds")
        return self.answers[index].left
    
    def get_answer_right(self, index):
        if index >= len(self.answers):
            raise Exception("Given index is out of bounds")
        return self.answers[index].right

    def get_guess(self, index):
        if index >= len(self.answers):
            raise Exception("Given index is out of bounds")
        return self.answers[index].guess
