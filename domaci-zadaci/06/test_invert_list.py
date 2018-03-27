from solutions import invert_list

import unittest
import random

class TestInvertList(unittest.TestCase):
    def test_empty_list(self):
        in_list = []
        expected = []

        actual = invert_list(in_list)

        self.assertEqual(expected, actual)

    def test_single_element(self):
        in_list = [random.randint(0, 1000)]
        expected = in_list[:]

        actual = invert_list(in_list)
        self.assertEqual(expected, actual)

    def test_odd_num_of_elements(self):
        in_list = [random.randint(0, 1000) for _ in range(10001)]
        expected = in_list[::-1]

        actual = invert_list(in_list)
        self.assertEqual(expected, actual)

    def test_even_num_of_elements(self):
        in_list = [random.randint(0, 1000) for _ in range(10000)]
        expected = in_list[::-1]

        actual = invert_list(in_list)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
