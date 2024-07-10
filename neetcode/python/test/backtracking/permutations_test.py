import unittest
from src.backtracking.permutations import Solution

class PermutationsTest(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,3]
        actual = sorted(Solution().permute(nums))
        expected = sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
        self.assertEqual(actual, expected)
