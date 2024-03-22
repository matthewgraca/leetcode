import unittest
from src.twopointers.trapping_rain_water import Solution

class TrappingRainWaterTest(unittest.TestCase):
    def test_example1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        actual = Solution.trap(height)
        expected = 6
        self.assertEqual(actual, expected)

    def test_example2(self):
        height = [4,2,0,3,2,5]
        actual = Solution.trap(height)
        expected = 9
        self.assertEqual(actual, expected)

    def test_example3(self):
        height = [5,2,0,3,2,4]
        actual = Solution.trap(height)
        expected = 9
        self.assertEqual(actual, expected)

    def test_example4(self):
        height = [5,4,1,2]
        actual = Solution.trap(height)
        expected = 1
        self.assertEqual(actual, expected)
