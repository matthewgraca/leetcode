import unittest
from src.stack.valid_parentheses import Solution

class ValidParenthesesTest(unittest.TestCase):
    def test_example1(self):
        s = "()"
        actual = Solution.isValid(s)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        s = "()[]{}"
        actual = Solution.isValid(s)
        expected = True
        self.assertEqual(actual, expected)

    def test_example3(self):
        s = "(]"
        actual = Solution.isValid(s)
        expected = False 
        self.assertEqual(actual, expected)

    def test_example4(self):
        s = "("
        actual = Solution.isValid(s)
        expected = False 
        self.assertEqual(actual, expected)

    def test_example5(self):
        s = "(("
        actual = Solution.isValid(s)
        expected = False 
        self.assertEqual(actual, expected)
