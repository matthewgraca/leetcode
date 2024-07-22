import unittest
from src.graphs.max_area_of_island import Solution

class MaxAreaOfIslandTest(unittest.TestCase):
    def test_example1(self):
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        actual = Solution().maxAreaOfIsland(grid)
        expected = 6
        self.assertEqual(actual, expected)

    def test_example2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        actual = Solution().maxAreaOfIsland(grid)
        expected = 0
        self.assertEqual(actual, expected)
