import unittest
from src.view.view_helpers import get_answer_label, get_new_game, get_equation_label
from src.model.classes.answer import Answer

class TestViewHelpers(unittest.TestCase):

    def test_get_new_game(self):
        
        test_game_1 = get_new_game(9, 1)
        test_game_2 = get_new_game(5, 2)

        """
        Test that game has the correct number of equations
        """        
        self.assertEqual(len(test_game_1.equation_list), 1)
        self.assertEqual(len(test_game_2.equation_list), 2)

    def test_get_equation_label(self):
        self.assertEqual(get_equation_label(1, 2), "1 x 2")
        self.assertEqual(get_equation_label(3, 0), "3 x 0")

    def test_get_answer_label(self):
        test_answer_1 = Answer(1, 2, 2)
        test_answer_2 = Answer(3, 6, 1)

        self.assertEqual(get_answer_label(test_answer_1, False), "1 x 2 = 2")
        self.assertEqual(get_answer_label(test_answer_2, True), "3 x 6 = 18, guess: 1")

