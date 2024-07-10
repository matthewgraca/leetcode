import unittest
from src.backtracking.combination_sum import Solution

class CombinationSumTest(unittest.TestCase):
    def test_example1(self):
        candidates, target = [2,3,6,7], 7
        actual = Solution().combinationSum(candidates, target)
        expected = [[2,2,3],[7]]
        self.assertEqual(actual, expected)
