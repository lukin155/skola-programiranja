from solutions import sub_str

import unittest

class TestSubStr(unittest.TestCase):
    def test_not_contained(self):
        big = "ABCD EFG"
        sub = "qqq"

        expected = []
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_one_in_one_positive(self):
        big = "z"
        sub = "z"

        expected = [0]
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_one_in_one_negative(self):
        big = "z"
        sub = "p"

        expected = []
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_one_in_many_positive(self):
        big = "z asdf zz qqq z qwerty"
        sub = "z"

        expected = [0, 7, 8, 14]
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_one_in_many_negative(self):
        big = "a asdf bv qqq g qwerty"
        sub = "z"

        expected = []
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_many_in_many_positive(self):
        big = "sss PJ2000 asdf qwerty PJ2000 abc de fgh"
        sub = "PJ2000"

        expected = [4, 23]
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_many_in_many_negative(self):
        big = "sss PJ2000 asdf qwerty PJ2000 abc de fgh"
        sub = "PJ2001"

        expected = []
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_equal_strings(self):
        big = "my string"
        sub = "my string"

        expected = [0]
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_multiplied(self):
        sub = "my string"
        big = 5 * sub

        expected = list(range(0, 5 * len(sub), len(sub)))
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

    def test_overlapping(self):
        big = "ttttssttt"
        sub = "ttt"

        expected = [0, 1, 6]
        actual = sub_str(big, sub)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
