import unittest
from src.graphs.islands_and_treasure import Solution

class IslandsAndTreasureTest(unittest.TestCase):
    def test_example1(self):
        grid = [
          [2147483647,-1,0,2147483647],
          [2147483647,2147483647,2147483647,-1],
          [2147483647,-1,2147483647,-1],
          [0,-1,2147483647,2147483647]
        ]
        Solution().islandsAndTreasure(grid)
        actual = grid
        expected = [
          [3,-1,0,1],
          [2,2,1,-1],
          [1,-1,2,-1],
          [0,-1,3,4]
        ]
        self.assertEqual(actual, expected)

    def test_example2(self):
        grid = [
          [0,-1],
          [2147483647,2147483647]
        ]
        Solution().islandsAndTreasure(grid)
        actual = grid
        expected =  [
          [0,-1],
          [1,2]
        ]       
        self.assertEqual(actual, expected)

    def test_example3(self):
        grid = [
          [0,2147483647,-1,0],
          [2147483647,2147483647,2147483647,2147483647]
        ]
        Solution().islandsAndTreasure(grid)
        actual = grid
        expected =  [
          [0,1,-1,0],
          [1,2,2,1]
        ]       
        self.assertEqual(actual, expected)
