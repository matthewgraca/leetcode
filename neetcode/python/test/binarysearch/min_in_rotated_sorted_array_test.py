import unittest
from src.binarysearch.min_in_rotated_sorted_array import Solution

class MinInRotatedSortedArrayTest(unittest.TestCase):
    def test_example1(self):
        nums = [3,4,5,1,2]
        actual = Solution().findMin(nums)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [4,5,6,7,0,1,2]
        actual = Solution().findMin(nums)
        expected = 0
        self.assertEqual(actual, expected)

    def test_example3(self):
        nums = [11,13,15,17]
        actual = Solution().findMin(nums)
        expected = 11
        self.assertEqual(actual, expected)

    def test_example4(self):
        nums = [2,1]
        actual = Solution().findMin(nums)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example5(self):
        nums = [3,1,2]
        actual = Solution().findMin(nums)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example6(self):
        nums = [5,1,2,3,4]
        actual = Solution().findMin(nums)
        expected = 1
        self.assertEqual(actual, expected)
