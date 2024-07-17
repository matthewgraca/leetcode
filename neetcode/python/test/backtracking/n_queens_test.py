import unittest
from src.backtracking.n_queens import Solution

class NQueensTest(unittest.TestCase):
    def test_example1(self):
        n = 4
        actual = Solution().solveNQueens(n)
        expected = [
            [".Q..","...Q","Q...","..Q."],
            ["..Q.","Q...","...Q",".Q.."]
        ]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        n = 1
        actual = Solution().solveNQueens(n)
        expected = [
            ["Q"]
        ]
        self.assertEqual(sorted(actual), sorted(expected))
