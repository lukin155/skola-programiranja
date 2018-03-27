from solutions import list_max_two

import unittest
import random

class TestListMax(unittest.TestCase):
    def test_two_equal_elements(self):
        in_list = [random.randint(0, 1000)] * 2

        expected = (in_list[0], in_list[1])
        actual = list_max_two(in_list)

        self.assertEqual(expected, actual)

    def test_two_different_elements(self):
        num = random.randint(0, 1000)

        expected = (num, num - 1)

        in_list = [num, num - 1]
        actual = list_max_two(in_list)
        self.assertEqual(expected, actual)

        in_list = [num - 1, num]
        actual = list_max_two(in_list)
        self.assertEqual(expected, actual)

    def test_random(self):
        in_list = [1e6 * random.random() for _ in range(100000)]

        sorted_list = in_list[:]
        sorted_list.sort()

        expected = (sorted_list[-1], sorted_list[-2])
        actual = list_max_two(in_list)
        print(len(in_list))
        print(in_list[:100])

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
