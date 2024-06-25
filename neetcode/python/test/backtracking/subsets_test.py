import unittest
from src.backtracking.subsets import Solution

class SubsetsTest(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,3]
        actual = sorted(Solution().subsets(nums))
        expected = sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [0]
        actual = sorted(Solution().subsets(nums))
        expected = sorted([[],[0]])
        self.assertEqual(actual, expected)
