import unittest
from src.heap.k_closest_points_to_origin import Solution

class KClosestPointsToOriginTest(unittest.TestCase):
    def test_example1(self):
        points, k = [[1,3],[-2,2]], 1
        actual = Solution().kClosest(points, k)
        expected = [[-2,2]]
        self.assertEqual(actual, expected)

    def test_example2(self):
        points, k = [[3,3],[5,-1],[-2,4]], 2
        actual = sorted(Solution().kClosest(points, k))
        expected = sorted([[3,3],[-2,4]])
        self.assertEqual(actual, expected)
