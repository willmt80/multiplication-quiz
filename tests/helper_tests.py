import unittest
from src.model.helpers import create_times_table, get_equation_list

class TestHelpers(unittest.TestCase):

    def test_create_tuple_list(self):
        
        test_list_1 = create_times_table(5)
        test_list_2 = create_times_table(9)

        """
        Test that the tuple list is the correct length
        """
        self.assertEqual(len(test_list_1), 36)
        self.assertEqual(len(test_list_2), 100)

        """
        Test that the tuple list has the correct values
        """
        for i in range(6):
            with self.subTest(i=i):
                message = "at index " + str(i)
                self.assertEqual(test_list_1[i].left, i//6, message)
                self.assertEqual(test_list_1[i].right, i%6, message)

        for i in range(10):
            with self.subTest(i=i):
                message = "at index " + str(i)
                self.assertEqual(test_list_2[i].left, i//10, message)
                self.assertEqual(test_list_2[i].right, i%10, message)

    def test_get_equation_list(self):
        test_list_1 = get_equation_list(create_times_table(5), 45)
        test_list_2 = get_equation_list(create_times_table(9), 90)

        """
        Test that the equation list is the correct length
        """
        self.assertEqual(len(test_list_1), 45)
        self.assertEqual(len(test_list_2), 90)

        
if __name__ == '__main__':
    unittest.main()