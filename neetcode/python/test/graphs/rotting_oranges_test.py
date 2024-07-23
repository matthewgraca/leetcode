import unittest
from src.graphs.rotting_oranges import Solution

class RottingOrangesTest(unittest.TestCase):
    def test_example1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        actual = Solution().orangesRotting(grid)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        actual = Solution().orangesRotting(grid)
        expected = -1
        self.assertEqual(actual, expected)

    def test_example3(self):
        grid = [[0,2]]
        actual = Solution().orangesRotting(grid)
        expected = 0
        self.assertEqual(actual, expected)

    def test_example4(self):
        grid = [[0]]
        actual = Solution().orangesRotting(grid)
        expected = 0
        self.assertEqual(actual, expected)
