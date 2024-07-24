import unittest
from src.graphs.pacific_atlantic_water_flow import Solution

class PacificAtlanticWaterFlowTest(unittest.TestCase):
    def test_example1(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        actual = Solution().pacificAtlantic(heights)
        expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        heights = [[1]]
        actual = Solution().pacificAtlantic(heights)
        expected = [[0,0]]
        self.assertEqual(sorted(actual), sorted(expected))
