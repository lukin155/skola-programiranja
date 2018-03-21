from solutions import is_palindrome

import unittest

class TestIsPalindrome(unittest.TestCase):
    
    # Test a palindrome with an even number of characters
    def test_positive_even(self):
        teststr = "abcddcba"
        
        expected = True
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)

    # Test a palindrome with an odd number of characters
    def test_positive_odd(self):
        teststr = "abcdcba"

        expected = True
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)

    # Test a non-palindrome with an even number of characters
    def test_negative_even(self):
        teststr = "abcdefgh"
        
        expected = False
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)

    # Test a non-palindrome with an odd number of characters
    def test_negative_odd(self):
        teststr = "abcdefg"
        
        expected = False
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)

    # Test a one-character string (every one-character string is a palindrome)
    def test_one_character(self):
        teststr = "a"

        expected = True
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)

    def test_empty_string(self):
        teststr = ""

        expected = True
        actual = is_palindrome(teststr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
