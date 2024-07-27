import unittest
from src.graphs.num_of_connected_components_in_an_undirected_graph import Solution

class NumOfConnectedComponentsInAnUndirectedGraphTest(unittest.TestCase):
    def test_example1(self):
        n = 3
        edges = [[0,1], [0,2]]
        actual = Solution().countComponents(n, edges)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example2(self):
        n = 6
        edges = [[0,1], [1,2], [2,3], [4,5]]
        actual = Solution().countComponents(n, edges)
        expected = 2
        self.assertEqual(actual, expected)
