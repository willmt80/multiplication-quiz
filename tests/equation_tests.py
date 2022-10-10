import unittest
from src.model.classes.equation import Equation
from src.model.classes.answer import Answer

class TestEquation(unittest.TestCase):
    def test_get_correct_answer(self):
        test_equation_1 = Equation(0, 0)
        test_equation_2 = Equation(5, 6)

        """
        Test that equation multiplication is correct
        """
        self.assertEqual(test_equation_1.get_correct_answer(), 0)
        self.assertEqual(test_equation_2.get_correct_answer(), 30)

    def test_equation_equality(self):
        test_equation_1 = Equation(0, 0)
        test_equation_2 = Equation(5, 6)

        """
        Test equation equality
        """
        self.assertEqual(test_equation_1, Equation(0, 0))
        self.assertEqual(test_equation_2, Equation(5, 6))
        self.assertNotEqual(test_equation_2, Equation(0, 0))
        self.assertNotEqual(test_equation_2, Equation(5, 5))
        self.assertNotEqual(test_equation_2, Equation(6, 6))
        self.assertNotEqual(test_equation_1, [0, 0])
        self.assertNotEqual(test_equation_1, Answer(0, 0, 0))
    
    def test_answer_equality(self):
        test_answer_1 = Answer(0, 0, 0)
        test_answer_2 = Answer(5, 6, 15)
        
        """
        Test answer equality
        """
        message_test_1 = "left " + str(test_answer_1.left) + " right " + str(test_answer_1.right) + " guess " + str(test_answer_1.guess)
        self.assertEqual(test_answer_1, Answer(0, 0, 0), message_test_1)
        self.assertEqual(test_answer_2, Answer(5, 6, 15))
        self.assertNotEqual(test_answer_1, Answer(5, 6, 15))
        self.assertNotEqual(test_answer_2, Answer(5, 6, 20))
        self.assertNotEqual(test_answer_2, Equation(5, 6))