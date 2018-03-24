from solutions import solve_quadratic_equation

import unittest

class TestSolveQuadraticEquation(unittest.TestCase):
    def test_1(self):
        a = 2
        b = 5
        c = -3

        expected = (-3, 0.5)
        actual = solve_quadratic_equation(a, b, c)

        self.assertEqual(expected, actual)

    def test_2(self):
        a = 1
        b = 3
        c = 2

        expected = (-2, -1)
        actual = solve_quadratic_equation(a, b, c)

        self.assertEqual(expected, actual)

    def test_3(self):
        a = 2
        b = -3
        c = -5

        expected = (-1, 2.5)
        actual = solve_quadratic_equation(a, b, c)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
