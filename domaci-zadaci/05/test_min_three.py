from solutions import min_three

import unittest
import random

class TestMinThree(unittest.TestCase):
    def test_1000_cases(self):
        for _ in range(1000):
            first = (random.random() - 0.5) * 2000
            second = (random.random() - 0.5) * 2000
            third = (random.random() - 0.5) * 2000

            expected = min(first, second, third)
        
            actual = min_three(first, second, third)
            self.assertEqual(expected, actual)

            actual = min_three(first, third, second)
            self.assertEqual(expected, actual)

            actual = min_three(second, first, third)
            self.assertEqual(expected, actual)

            actual = min_three(second, third, first)
            self.assertEqual(expected, actual)

            actual = min_three(third, first, second)
            self.assertEqual(expected, actual)

            actual = min_three(third, second, first)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
