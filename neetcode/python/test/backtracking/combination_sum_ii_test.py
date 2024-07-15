import unittest
from src.backtracking.combination_sum_ii import Solution

class CombinationSumIITest(unittest.TestCase):
    def test_example1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        actual = Solution().combinationSum2(candidates, target)
        expected = [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
        ]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        candidates = [2,5,2,1,2]
        target = 5
        actual = Solution().combinationSum2(candidates, target)
        expected = [
            [1,2,2],
            [5]
        ]
        self.assertEqual(sorted(actual), sorted(expected))
