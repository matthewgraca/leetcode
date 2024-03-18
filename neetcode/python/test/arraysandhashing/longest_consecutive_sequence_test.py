import unittest
from typing import List
from src.arraysandhashing.longest_consecutive_sequence import Solution

class LongestConsecutiveSequenceTest(unittest.TestCase):
    def test_example1(self):
        nums = [100,4,200,1,3,2]
        actual = Solution.longestConsecutive(nums)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        actual = Solution.longestConsecutive(nums)
        expected = 9
        msg = "The input contains duplicates that should not be counted"
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        nums = [0,1,5,6,7,8,9]
        actual = Solution.longestConsecutive(nums)
        expected = 5
        msg = "There are two sequences; the smaller is 2, the larger is 5"
        self.assertEqual(actual, expected, msg)

