import unittest
from src.binarysearch.binary_search import Solution

class BinarySearchTest(unittest.TestCase):
    def test_example1(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        actual = Solution().search(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        actual = Solution().search(nums, target)
        expected = -1
        self.assertEqual(actual, expected)
