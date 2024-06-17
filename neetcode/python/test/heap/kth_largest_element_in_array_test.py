import unittest
from src.heap.kth_largest_element_in_array import Solution

class KthLargestElementInArrayTest(unittest.TestCase):
    def test_example1(self):
        nums, k = [3,2,1,5,6,4], 2
        actual = Solution().findKthLargest(nums, k)
        expected = 5
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums, k = [3,2,3,1,2,4,5,5,6], 4
        actual = Solution().findKthLargest(nums, k)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example3(self):
        nums, k = [2,1], 2 
        actual = Solution().findKthLargest(nums, k)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example4(self):
        nums, k = [1], 1 
        actual = Solution().findKthLargest(nums, k)
        expected = 1
        self.assertEqual(actual, expected)


