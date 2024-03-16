import unittest
from typing import List
from src.arraysandhashing.top_k_frequent_elements import Solution

class TopKFrequentElementsTest(unittest.TestCase):
    def test_example1(self):
       nums = [1,1,1,2,2,3]
       k = 2
       actual = Solution.topKFrequent(nums, k)
       expected = [1,2]
       self.assertEqual(actual, expected)

    def test_example2(self):
       nums = [1]
       k = 1
       actual = Solution.topKFrequent(nums, k)
       expected = [1]
       self.assertEqual(actual, expected)
