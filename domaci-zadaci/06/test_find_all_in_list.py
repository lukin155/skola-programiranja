from solutions import find_all_in_list

import unittest
import random

class TestFindAllInList(unittest.TestCase):
    def test_not_contained(self):
        in_list = [1, 2, 3, 4, 5]
        el = 10

        expected = []
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_empty_list(self):
        in_list = []
        el = random.randint(-10000, 10000)

        expected = []
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_one_element_negative(self):
        in_list = [-1]
        el = random.randint(0, 10000)

        expected = []
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_one_element_positive(self):
        in_list = [3]
        el = 3

        expected = [0]
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_multiple_same_elements_negative(self):
        in_list = [-1] * random.randint(0, 1000)
        el = random.randint(0, 1000)

        expected = []
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_multiple_same_elements_positive(self):
        num_elements = random.randint(0, 1000)
        in_list = [3] * num_elements
        el = 3

        expected = list(range(0, num_elements))
        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_random_positive(self):
        el = 3
        expected = []
        in_list = []

        # Generate a list of 10000 elements
        for i in range(0, 10000):
            # Each element will be an int between el - 5 and el + 5, some (roughly 10%) are bound to be equal el
            new_el = random.randint(el - 5, el + 5)
            in_list.append(new_el)
            # Save the positions of those that are equal to el
            if new_el == el:
                expected.append(i)

        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_random_negative(self):
        el = -1
        expected = []
        in_list = []

        # Generate a list of 10000 elements
        for _ in range(0, 10000):
            new_el = random.randint(0, 1000)
            in_list.append(new_el)

        actual = find_all_in_list(in_list, el)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
