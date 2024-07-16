import unittest
from src.backtracking.palindrome_partitioning import Solution

class PalindromePartitioningTest(unittest.TestCase):
    def test_example1(self):
        s = "aab"
        actual = Solution().partition(s)
        expected = [["a","a","b"],["aa","b"]]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        s = "a"
        actual = Solution().partition(s)
        expected = [["a"]]
        self.assertEqual(sorted(actual), sorted(expected))
