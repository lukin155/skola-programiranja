from solutions import square_circumference_and_area

import unittest
import random

class TestSquareCircumferenceAndArea(unittest.TestCase):
    def test_1(self):
        side = 1

        expected = (4, 1)
        actual = square_circumference_and_area(side)

        self.assertEqual(expected, actual)

    def test_random_int(self):
        side = random.randint(0, 1000)

        expected = (4 * side, side * side)
        actual = square_circumference_and_area(side)

        self.assertEqual(expected, actual)

    def test_random_float(self):
        side = random.random() * 1000 # random() returns a number from [0,1) which we multiply by 1000 to get a float from [0, 1000)

        expected = (4 * side, side * side)
        actual = square_circumference_and_area(side)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
