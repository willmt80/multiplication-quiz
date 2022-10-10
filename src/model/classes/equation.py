class Equation:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def get_correct_answer(self):
        return self.left * self.right

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.left == other.left and \
               self.right == other.right