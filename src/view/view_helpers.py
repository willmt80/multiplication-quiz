from src.model.classes.answer import Answer
from src.model.helpers import create_times_table, get_equation_list
from src.model.classes.game_state import GameState
# from src.model.classes.answer import Answer

def get_new_game(max: int, count: int):
    times_table = create_times_table(max)
    return GameState(get_equation_list(times_table, count))

def get_equation_label(left: int, right: int):
    return str(left) + " x " + str(right)

def get_answer_label(answer: Answer, with_guess: bool):
    label = get_equation_label(answer.left, answer.right) + " = " + str(answer.get_correct_answer())
    if with_guess:
        label = label + ", guess: " + str(answer.guess)
    return label