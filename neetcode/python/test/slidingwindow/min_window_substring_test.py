import unittest
from src.slidingwindow.min_window_substring import Solution

class MinWindowSubstringTest(unittest.TestCase):
    def test_example1(self):
        s,t = "ADOBECODEBANC", "ABC"
        actual = Solution.minWindow(s,t)
        expected = "BANC"
        self.assertEqual(actual,expected)

    def test_example2(self):
        s,t = "a", "a"
        actual = Solution.minWindow(s,t)
        expected = "a"
        self.assertEqual(actual,expected)

    def test_example3(self):
        s,t = "a", "aa"
        actual = Solution.minWindow(s,t)
        expected = ""
        self.assertEqual(actual,expected)

    def test_example4(self):
        s,t = "aa", "aa"
        actual = Solution.minWindow(s,t)
        expected = "aa"
        self.assertEqual(actual,expected)
