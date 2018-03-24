from solutions import rectangle_circumference_and_area

import unittest
import random

class TestSquareCircumferenceAndArea(unittest.TestCase):
    def test_random_int(self):
        sidea = random.randint(0, 1000)
        sideb = random.randint(0, 1000)

        expected = (2 * sidea + 2 * sideb, sidea * sideb)
        actual = rectangle_circumference_and_area(sidea, sideb)

        self.assertEqual(expected, actual)

    def test_random_float(self):
        # random() returns a number from [0,1) which we multiply by 1000 to get a float from [0, 1000)
        sidea = random.random() * 1000
        sideb = random.random() * 1000

        expected = (2 * sidea + 2 * sideb, sidea * sideb)
        actual = rectangle_circumference_and_area(sidea, sideb)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
