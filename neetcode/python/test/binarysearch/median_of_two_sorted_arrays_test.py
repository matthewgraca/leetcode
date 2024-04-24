import unittest
from src.binarysearch.median_of_two_sorted_arrays import Solution

class MedianOfTwoSortedArraysTest(unittest.TestCase):
    def test_example1(self):
        nums1 = [1,3]
        nums2 = [2]
        actual = Solution().findMedianSortedArrays(nums1, nums2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums1 = [1,2]
        nums2 = [3,4]
        actual = Solution().findMedianSortedArrays(nums1, nums2)
        expected = 2.5
        self.assertEqual(actual, expected)
