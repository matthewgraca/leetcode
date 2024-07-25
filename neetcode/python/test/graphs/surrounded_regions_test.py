import unittest
from src.graphs.surrounded_regions import Solution

class SurroundedRegionsTest(unittest.TestCase):
    def test_example1(self):
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        Solution().solve(board)
        actual = board
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        self.assertEqual(actual, expected)

    def test_example2(self):
        board = [["X"]]
        Solution().solve(board)
        actual = board
        expected = [["X"]]
        self.assertEqual(actual, expected)

    def test_example3(self):
        board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        Solution().solve(board)
        actual = board
        expected = [["O","O","O"],["O","O","O"],["O","O","O"]]
        self.assertEqual(actual, expected)
