from solutions import input_list # you can adjust the file name from solutions(.py) to something else

import unittest
import random

class TestInputList(unittest.TestCase):
    def test_simple_one_digit(self):
        input_string = "1,2,3,4,5"
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(expected, actual)

    def test_simple_one_digit_negative_numbers(self):
        input_string = "1,-2,3,-4,5"
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = [1, -2, 3, -4, 5]

        self.assertEqual(expected, actual)

    def test_simple_column_delim(self):
        input_string ="1;2;3;4;5"
        delimiter = ";"

        actual = input_list(input_string, delimiter)
        expected = [1, 2, 3, 4, 5]

        self.assertEqual(actual, expected)

    def test_simple_multiple_digits(self):
        input_string = "1,23,456,78,9"
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = [1, 23, 456, 78, 9]

        self.assertEqual(actual, expected)

    def test_single_element_one_digit(self):
        input_string = "1"
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = [1]

        self.assertEqual(actual, expected)

    def test_single_element_multiple_digits(self):
        input_string = "987"
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = [987]

        self.assertEqual(actual, expected)

    def test_empty_string(self):
        input_string = ""
        delimiter = ","

        actual = input_list(input_string, delimiter)
        expected = []

        self.assertEqual(actual, expected)

    def test_random_positive_numbers(self):
        rand_list = [random.randint(0, 1e6) for i in range(100)]

        delimiter = ","

        input_string = delimiter.join(map(str, rand_list))

        expected = rand_list
        actual = input_list(input_string, delimiter)

        self.assertEqual(actual, expected)

    def test_random_positive_and_negative_numbers(self):
        rand_list = [random.randint(-1e6, 1e6) for i in range(100)]

        delimiter = ","

        input_string = delimiter.join(map(str, rand_list))

        expected = rand_list
        actual = input_list(input_string, delimiter)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
