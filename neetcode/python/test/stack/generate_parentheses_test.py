import unittest
from src.stack.generate_parentheses import Solution

class GenerateParenthesesTest(unittest.TestCase):
    def test_example1(self):
        n = 3
        actual = sorted(Solution().generateParenthesis(n))
        expected = sorted(["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(actual, expected)

    def test_example2(self):
        n = 1
        actual = Solution().generateParenthesis(n)
        expected = ["()"]
        self.assertEqual(actual, expected)
