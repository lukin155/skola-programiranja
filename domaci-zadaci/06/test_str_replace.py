from solutions import str_replace

import unittest

class TestStrReplace(unittest.TestCase):
    def test_nothing_to_replace(self):
        in_str = "My string bla bla"
        find = "not contained"
        replace = "some string"

        expected = in_str
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_replace_smaller_with_bigger(self):
        in_str = "My string bla"
        find = "My"
        replace = "Your"

        expected = "Your string bla"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_replace_bigger_with_smaller(self):
        in_str = "My string bla"
        find = "string"
        replace = "bla"

        expected = "My bla bla"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_replace_multiple_smaller_with_bigger(self):
        in_str = "My string My bla My My"
        find = "My"
        replace = "Your"

        expected = "Your string Your bla Your Your"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_replace_multiple_bigger_with_smaller(self):
        in_str = "string my string bla"
        find = "string"
        replace = "bla"

        expected = "bla my bla bla"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_overlapping(self):
        in_str = "AAAAA"
        find = "AA"
        replace = "NEW"

        expected = "NEWNEWA"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_joint(self):
        in_str = "oldoldold oldold"
        find = "old"
        replace = "new"

        expected = "newnewnew newnew"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_no_spaces(self):
        in_str = "abcdabvgabcqwsabcabc"
        find = "abc"
        replace = "123456789"

        expected = "123456789dabvg123456789qws123456789123456789"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_empty_in_str(self):
        in_str = ""
        find = "asdf"
        replace = "qqq"

        expected = ""
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

    def test_empty_replace(self):
        in_str = "My string bla"
        find = "My "
        replace = ""

        expected = "string bla"
        actual = str_replace(in_str, find, replace)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
