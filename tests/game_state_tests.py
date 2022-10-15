import unittest
from src.model.classes.answer import Answer
from src.model.classes.game_state import GameState
from src.model.classes.equation import Equation

class GameTests(unittest.TestCase):
    def test_game_state_methods(self):
        test_game_state = GameState([Equation(0, 0), Equation(1, 1), Equation(4, 5)])

        """
        Test that game state guesses are recorded properly
        """
        self.assertEqual(test_game_state.get_current_equation(), Equation(0, 0))

        # First guess
        test_game_state.make_guess(1)
        self.assertTrue(test_game_state.do_equations_remain())
        self.assertEqual(test_game_state.get_current_equation(), Equation(1, 1))
        self.assertListEqual(test_game_state.answers, [Answer(0, 0, 1)])

        # Second guess
        test_game_state.make_guess(1)
        self.assertTrue(test_game_state.do_equations_remain())
        self.assertEqual(test_game_state.get_current_equation(), Equation(4, 5))
        self.assertEqual(test_game_state.get_cur_left(), 4)
        self.assertEqual(test_game_state.get_cur_right(), 5)
        self.assertListEqual(test_game_state.answers, [Answer(0, 0, 1), Answer(1, 1, 1)])

        # Third guess
        test_game_state.make_guess(5)
        self.assertFalse(test_game_state.do_equations_remain())
        self.assertListEqual(test_game_state.answers, [Answer(0, 0, 1), Answer(1, 1, 1), Answer(4, 5, 5)])
        self.assertEqual(test_game_state.get_answer_left(0), 0)
        self.assertEqual(test_game_state.get_answer_right(1), 1)
        self.assertEqual(test_game_state.get_guess(2), 5)
        
        # Exceptions since all equations have been answered
        with self.assertRaises(Exception) as context:
            test_game_state.get_current_equation()
        self.assertTrue("All equations have been answered" in str(context.exception))

        with self.assertRaises(Exception) as context:
            test_game_state.make_guess(2)
        self.assertTrue("All equations have been answered" in str(context.exception))

        with self.assertRaises(Exception) as context:
            test_game_state.get_cur_right()
        self.assertTrue("All equations have been answered" in str(context.exception))

        with self.assertRaises(Exception) as context:
            test_game_state.get_cur_left()
        self.assertTrue("All equations have been answered" in str(context.exception))

        with self.assertRaises(Exception) as context:
            test_game_state.get_answer_left(3)
        self.assertTrue("Given index is out of bounds" in str(context.exception))
        