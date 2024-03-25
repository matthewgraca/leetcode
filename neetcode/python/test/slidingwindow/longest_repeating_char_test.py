import unittest
from src.slidingwindow.longest_repeating_char import Solution

class LongestRepeatingCharTest(unittest.TestCase):
    def test_example1(self):
        s = "ABAB"
        k = 2
        actual = Solution.characterReplacement(s,k)
        expected = 4
        msg = (
            f"For \"{s}\" with k = {k}, replace the two \"A\"s with two \"B\"s"
            ", or vice versa"
        )
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        s = "AABABBA"
        k = 1
        actual = Solution.characterReplacement(s,k)
        expected = 4
        msg = (
            f"Replace the one \'A\' in the middle with \'B\' and form "
            "\"AABBBBA\". The substring \"BBBB\" has the longest repeating " 
            "letters, which is 4.\n" 
            "There may exist other ways to achieve this answer too."
        )
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        s = "AAAB"
        k = 0
        actual = Solution.characterReplacement(s,k)
        expected = 3
        msg = (
            ""
        )
        self.assertEqual(actual, expected, msg)
        
    def test_example4(self):
        s = "ABAA"
        k = 0
        actual = Solution.characterReplacement(s,k)
        expected = 2
        msg = (
            ""
        )
        self.assertEqual(actual, expected, msg)

    def test_example5(self):
        s = "ABBB"
        k = 2
        actual = Solution.characterReplacement(s,k)
        expected = 4
        msg = (
            ""
        )
        self.assertEqual(actual, expected, msg)
