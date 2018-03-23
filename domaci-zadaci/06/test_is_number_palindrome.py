from solutions import is_number_palindrome

import unittest

class TestIsNumberPalindrome(unittest.TestCase):
    # Test a palindrome with an even number of digits
    def test_positive_even(self):
        testnum = 123321
        
        expected = True
        actual = is_number_palindrome(testnum)

        self.assertEqual(expected, actual)

    # Test a palindrome with an odd number of digits
    def test_positive_odd(self):
        testnum = 123454321

        expected = True
        actual = is_number_palindrome(testnum)

        self.assertEqual(expected, actual)

    # Test a non-palindrome with an even number of digits
    def test_negative_even(self):
        testnum = 1234
        
        expected = False
        actual = is_number_palindrome(testnum)

        self.assertEqual(expected, actual)

    # Test a non-palindrome with an odd number of digits
    def test_negative_odd(self):
        testnum = 123
        
        expected = False
        actual = is_number_palindrome(testnum)

        self.assertEqual(expected, actual)

    # Test a one-digits number (every one-digits number is a palindrome)
    def test_one_character(self):
        testnum = 3

        expected = True
        actual = is_number_palindrome(testnum)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
