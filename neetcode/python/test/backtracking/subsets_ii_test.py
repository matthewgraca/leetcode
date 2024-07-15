import unittest
from src.backtracking.subsets_ii import Solution

class SubsetsIITest(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,2]
        actual = Solution().subsetsWithDup(nums)
        expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        nums = [0]
        actual = Solution().subsetsWithDup(nums)
        expected = [[],[0]]
        self.assertEqual(sorted(actual), sorted(expected))
