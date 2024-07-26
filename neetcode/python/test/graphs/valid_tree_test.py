import unittest
from src.graphs.valid_tree import Solution

class ValidTreeTest(unittest.TestCase):
    def test_example1(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        actual = Solution().validTree(n, edges)
        expected = True
        self.assertEqual(actual, expected)

    def test_contains_cycle(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        actual = Solution().validTree(n, edges)
        expected = False 
        self.assertEqual(actual, expected)

    def test_contains_many_roots(self):
        n = 4
        edges = [[0,1], [2,3]]
        actual = Solution().validTree(n, edges)
        expected = False 
        self.assertEqual(actual, expected)
