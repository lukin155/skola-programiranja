from solutions import trim_str

import random
import unittest

class TestTrimStr(unittest.TestCase):
    # 0 leading spaces, 0 trailing spaces
    def test_00(self):
        teststr = "Test string."

        expected = teststr
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # 0 leading spaces, 1 trailing space
    def test_01(self):
        teststr = "Test string. "

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # 0 leading spaces, n trailing spaces
    def test_0n(self):
        teststr = "Test string." + (random.randint(0, 100) * " ")

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # 1 leading space, 0 trailing spaces
    def test_10(self):
        teststr = " Test string."

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # 1 leading space, 1 trailing space
    def test_11(self):
        teststr = " Test string. "

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # 1 leading space, n trailing spaces
    def test_1n(self):
        teststr = " Test string." + (random.randint(0, 100) * " ")

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # n leading spaces, 0 trailing spaces
    def test_n0(self):
        teststr = (random.randint(0, 100) * " ") + "Test string."

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # n leading spaces, 1 trailing space
    def test_n1(self):
        teststr = (random.randint(0, 100) * " ") + "Test string. "

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

    # n leading spaces, n trailing spaces
    def test_nn(self):
        teststr = (random.randint(0, 100) * " ") + "Test string." + (random.randint(0, 100) * " ")

        expected = "Test string."
        actual = trim_str(teststr)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
