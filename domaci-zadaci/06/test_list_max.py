from solutions import list_max

import unittest
import random

class TestListMax(unittest.TestCase):
    def test_single_element(self):
        in_list = [random.randint(0, 1000)]

        expected = in_list[0]
        actual = list_max(in_list)

        self.assertEqual(expected, actual)

    def test_random(self):
        in_list = [random.randint(0, 1000) for _ in range(0, 100000)]

        expected = max(in_list)
        actual = list_max(in_list)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
