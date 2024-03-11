import unittest
from src.arraysandhashing.two_sum import Solution
from typing import List

class TwoSumTest(unittest.TestCase):
    def test_example1(self):
        nums = [2,7,11,15]
        target = 9
        actual = Solution.twoSumNaive(nums, target)
        expected = [0,1]
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [3,2,4]
        target = 6
        actual = Solution.twoSumNaive(nums, target)
        expected = [1,2]
        self.assertEqual(actual, expected)

    def test_example3(self):
        nums = [3,3]
        target = 6
        actual = Solution.twoSumNaive(nums, target)
        expected = [0,1]
        self.assertEqual(actual, expected)

    def test_example1a(self):
        nums = [2,7,11,15]
        target = 9
        actual = Solution.twoSum(nums, target)
        expected = [0,1]
        self.assertEqual(actual, expected)

    def test_example2a(self):
        nums = [3,2,4]
        target = 6
        actual = Solution.twoSum(nums, target)
        expected = [1,2]
        self.assertEqual(actual, expected)

    def test_example3a(self):
        nums = [3,3]
        target = 6
        actual = Solution.twoSum(nums, target)
        expected = [0,1]
        self.assertEqual(actual, expected)

    def test_example4a(self):
        nums = [-3, 4, 3, 90]
        target = 0
        actual = Solution.twoSum(nums, target)
        expected = [0,2]
        self.assertEqual(actual, expected)
