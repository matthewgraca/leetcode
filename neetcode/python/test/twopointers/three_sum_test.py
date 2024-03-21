import unittest
from src.twopointers.three_sum import Solution

class ThreeSumTest(unittest.TestCase):
    def test_example1(self):
        nums = [-1,0,1,2,-1,-4]
        actual = Solution.threeSum(nums)
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [0,1,1]
        actual = Solution.threeSum(nums)
        expected = []
        msg = "No solution expected"
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        nums = [0,0,0]
        actual = Solution.threeSum(nums)
        expected = [[0,0,0]]
        msg = "Single valid solution"
        self.assertEqual(actual, expected, msg)

    def test_example4(self):
        nums = [0,0,0,0]
        actual = Solution.threeSum(nums)
        expected = [[0,0,0]]
        msg = "No duplicate solutions should exist"
        self.assertEqual(actual, expected, msg)
