import unittest
from src.stack.polish import Solution

class PolishTest(unittest.TestCase):
    def test_example1(self):
        tokens = ["2","1","+","3","*"]
        actual = Solution().evalRPN(tokens)
        expected = 9
        msg = "((2 + 1) * 3) = 9"
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        tokens = ["4","13","5","/","+"]
        actual = Solution().evalRPN(tokens)
        expected = 6
        msg = "(4 + (13 / 5)) = 6"
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        tokens = [
            "10","6","9","3","+","-11","*","/","*","17","+",
            "5","+"
        ]
        actual = Solution().evalRPN(tokens)
        expected = 22
        msg = (
            """((10 * (6 / ((9 + 3) * -11))) + 17) + 5\n
            = ((10 * (6 / (12 * -11))) + 17) + 5\n
            = ((10 * (6 / -132)) + 17) + 5\n
            = ((10 * 0) + 17) + 5\n
            = (0 + 17) + 5\n
            = 17 + 5\n
            = 22"""
        )
        self.assertEqual(actual, expected, msg)

    def test_example4(self):
        tokens = ["18"]
        actual = Solution().evalRPN(tokens)
        expected = 18
        self.assertEqual(actual, expected)
