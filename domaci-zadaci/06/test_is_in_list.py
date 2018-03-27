from solutions import is_in_list

import unittest
import random

class TestIInList(unittest.TestCase):
    def test_empty_list(self):
        in_list = []
        el = 0

        expected = False
        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_one_element_positive(self):
        el = random.random()
        in_list = [el]

        expected = True
        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_one_element_negative(self):
        el = random.random()
        in_list = [el + 0.5]

        expected = False
        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_multiple_same_elements_positive(self):
        el = random.random()
        in_list = [el] * random.randint(0, 1000)

        expected = True
        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_multiple_same_elements_negative(self):
        el = random.random()
        in_list = [el - 0.5] * random.randint(0, 1000)

        expected = False
        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_random_positive(self):
        el = 3
        expected = True
        in_list = []

        is_there = False

        # Generate a list of 10000 random int elements, between el - 5 and el + 5
        # Some of the elements (roughly 10%) should be equal to el
        for _ in range(0, 10000):
            new_el = random.randint(el - 5, el + 5)
            in_list.append(new_el)

            if new_el == el:
                is_there = True

        # If by some miracle none of the generated random numbers is equal to el, make sure there
        # is at least one el in the test list, by appending el to the end of the list
        if not is_there:
            print("It's a miracle!\n" * 1000)
            in_list.append(el)

        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

    def test_random_negative(self):
        el = -1
        expected = False

        # Generate a list of 10000 random int elements, between 0 and thousand (none of them will be equal to -1)
        in_list = [random.randint(0, 1000) for i in range(0, 10000)]

        actual = is_in_list(in_list, el)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
