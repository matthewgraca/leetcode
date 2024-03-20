import unittest
from src.twopointers.valid_palindrome import Solution

class ValidPalindromeTest(unittest.TestCase):
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        actual = Solution.isPalindrome(s)
        expected = True
        msg = "String is a palindrome removing non-alphanumeric characters ',', ' ', and ':'"
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        s = "race a car"
        actual = Solution.isPalindrome(s)
        expected = False 
        msg = "String is not a palindrome removing non-alphanumeric characters ' '"
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        s = " "
        actual = Solution.isPalindrome(s)
        expected = True 
        msg = "An empty string is a palindrome removing non-alphanumeric characters ' '"
        self.assertEqual(actual, expected, msg)

    def test_example4(self):
        s = "racecar"
        actual = Solution.isPalindrome(s)
        expected = True 
        msg = "String is a palindrome with an odd number of characters, with no non-alphanumeric characters"
        self.assertEqual(actual, expected, msg)

    def test_example5(self):
        s = "abba"
        actual = Solution.isPalindrome(s)
        expected = True 
        msg = "String is a palindrome with an even number of characters, with no non-alphanumeric characters"
        self.assertEqual(actual, expected, msg)
