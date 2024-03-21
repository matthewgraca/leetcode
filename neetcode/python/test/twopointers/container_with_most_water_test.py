import unittest
from src.twopointers.container_with_most_water import Solution

class ContainerWithMostWaterTest(unittest.TestCase):
    def test_example1(self):
        height = [1,8,6,2,5,4,8,3,7]
        actual = Solution.maxArea(height)
        expected = 49
        self.assertEqual(actual, expected)

    def test_example2(self):
        height = [1,1]
        actual = Solution.maxArea(height)
        expected = 1
        self.assertEqual(actual, expected)
        
    def test_example3(self):
        height = [1,2,4,3]
        actual = Solution.maxArea(height)
        expected = 4
        self.assertEqual(actual, expected)
 
