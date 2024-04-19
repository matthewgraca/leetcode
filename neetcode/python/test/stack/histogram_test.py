import unittest
from src.stack.histogram import Solution

class HistogramTest(unittest.TestCase):
    def test_example1(self):
        heights = [2,1,5,6,2,3]
        actual = Solution.largestRectangleArea(heights)
        expected = 10
        self.assertEqual(actual, expected)

    def test_example2(self):
        heights = [2,4]
        actual = Solution.largestRectangleArea(heights)
        expected = 4
        self.assertEqual(actual, expected)

