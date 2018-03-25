from solutions import is_vowel

import unittest

class TestIsVowel(unittest.TestCase):
    def test_positive_lower(self):
        expected = True

        for s in ["a", "e", "i", "o", "u"]:
            actual = is_vowel(s)
            self.assertEqual(expected, actual)

    def test_positive_upper(self):
        expected = True

        for s in ["A", "E", "I", "O", "U"]:
            actual = is_vowel(s)
            self.assertEqual(expected, actual)

    def test_negative_single_char(self):
        expected = False
        for s in ["B", "C", "D", "Q", "s", "p", "j", "n"]:
            actual = is_vowel(s)
            self.assertEqual(expected, actual)

    def test_negative_multiple_chars(self):
        expected = False
        for s in ["asdf", "aa", "aeiou", "ES", "QI", "PPP", "AA", "some string"]:
            actual = is_vowel(s)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
