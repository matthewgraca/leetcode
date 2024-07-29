import unittest
from src.graphs.redundant_connection import Solution

class RedundantConnectionTest(unittest.TestCase):
    def test_example1(self):
        edges = [[1,2],[1,3],[2,3]]
        actual = Solution().findRedundantConnection(edges)
        expected = [2,3]
        self.assertEqual(actual, expected)

    def test_example2(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        actual = Solution().findRedundantConnection(edges)
        expected = [1,4]
        self.assertEqual(actual, expected)

