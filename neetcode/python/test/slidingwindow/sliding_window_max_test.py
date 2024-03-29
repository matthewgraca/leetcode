import unittest
from src.slidingwindow.sliding_window_max import Solution

class SlidingWindowMaxTest(unittest.TestCase):
    def test_example1(self):
        nums, k = [1,3,-1,-3,5,3,6,7], 3
        actual = Solution.maxSlidingWindow(nums,k)
        expected = [3,3,5,5,6,7]
        self.assertEqual(actual,expected)

    def test_example2(self):
        nums, k = [1], 1
        actual = Solution.maxSlidingWindow(nums,k)
        expected = [1]
        self.assertEqual(actual,expected)
