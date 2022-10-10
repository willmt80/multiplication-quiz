from .equation import Equation

class Answer(Equation):
    def __init__(self, left: int, right: int, guess: int):
        super().__init__(left, right)
        self.guess = guess

    def __eq__(self, other):
        return super().__eq__(other) and \
               self.guess == other.guess
    