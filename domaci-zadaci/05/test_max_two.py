from solutions import max_two

import unittest
import random

class TestMaxTwo(unittest.TestCase):
    def test_neg_neg(self):
        first = random.random() * -1000
        second = random.random() * -1000

        expected = max(first, second)
        
        actual = max_two(first, second)
        self.assertEqual(expected, actual)

        actual = max_two(second, first)
        self.assertEqual(expected, actual)

    def test_neg_pos(self):
        first = random.random() * -1000
        second = random.random() * 1000

        expected = max(first, second)
        
        actual = max_two(first, second)
        self.assertEqual(expected, actual)

        actual = max_two(second, first)
        self.assertEqual(expected, actual)

    def test_pos_pos(self):
        first = random.random() * 1000
        second = random.random() * 1000

        expected = max(first, second)
        
        actual = max_two(first, second)
        self.assertEqual(expected, actual)

        actual = max_two(second, first)
        self.assertEqual(expected, actual)

    def test_1000_cases(self):
        for _ in range(1000):
            first = random.random() * 1000
            second = random.random() * 1000

            expected = max(first, second)
        
            actual = max_two(first, second)
            self.assertEqual(expected, actual)

            actual = max_two(second, first)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
