import unittest
from typing import List
from src.arraysandhashing.product_of_array_except_self import Solution

class ProductOfArrayExceptSelfTest(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,3,4]
        actual = Solution.productExceptSelf(nums)
        expected = [24,12,8,6]
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [-1,1,0,-3,3]
        actual = Solution.productExceptSelf(nums)
        expected = [0,0,9,0,0]
        self.assertEqual(actual, expected)
