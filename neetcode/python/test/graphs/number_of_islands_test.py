import unittest
from src.graphs.number_of_islands import Solution

class NumberOfIslandsTest(unittest.TestCase):
    def test_example1(self):
        grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        actual = Solution().numIslands(grid)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example2(self):
        grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        actual = Solution().numIslands(grid)
        expected = 3
        self.assertEqual(actual, expected)

    def test_example3(self):
        grid = [
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"]
        ]
        actual = Solution().numIslands(grid)
        expected = 0
        self.assertEqual(actual, expected)

    def test_example4(self):
        grid = [
            ["1","1","1"],
            ["0","1","0"],
            ["0","1","0"]
        ]
        actual = Solution().numIslands(grid)
        expected = 1
        self.assertEqual(actual, expected)
