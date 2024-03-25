import unittest
from src.slidingwindow.longest_substring import Solution

class LongestSubstringTest(unittest.TestCase):
    def test_example1(self):
        s = "abcabcbb"
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 3
        msg = (
            f"For the string \"{s}\", the substring is \"abc\""
        )
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        s = "bbbbb"
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 1
        msg = (
            f"For the string \"{s}\", the substring is \"b\""
        )
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        s = "pwwkew"
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 3
        msg = (
            f"For the string \"{s}\", the substring is \"wke\". "
            "Note that while \"pwke\" is a subsequence, "
            "it is not a substring (whose characters must be sequential)"
        )
        self.assertEqual(actual, expected, msg)

    def test_example4(self):
        s = " "
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 1
        msg = (
            f"For the string \"{s}\", the substring is \" \""
        )
        self.assertEqual(actual, expected, msg)

    def test_example5(self):
        s = "a"
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 1
        msg = (
            f"For the string \"{s}\", the substring is \"a\""
        )
        self.assertEqual(actual, expected, msg)

    def test_example6(self):
        s = "dvdf"
        actual = Solution.lengthOfLongestSubstring(s)
        expected = 3
        msg = (
            f"For the string \"{s}\", the substring is \"vdf\""
        )
        self.assertEqual(actual, expected, msg)
