import unittest
from src.binarysearch.search_matrix import Solution

class SearchMatrixTest(unittest.TestCase):
    def test_example1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        actual = Solution().searchMatrix(matrix, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        actual = Solution().searchMatrix(matrix, target)
        expected = False 
        self.assertEqual(actual, expected)
