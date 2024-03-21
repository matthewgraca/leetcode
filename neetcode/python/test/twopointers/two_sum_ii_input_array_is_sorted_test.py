import unittest
from src.twopointers.two_sum_ii_input_array_is_sorted import Solution

class TwoSumIIInputArrayIsSortedTest(unittest.TestCase):
    def test_example1(self):
        numbers = [2,7,11,15]
        target = 9
        actual = Solution.twoSum(numbers, target)
        expected = [1,2]
        msg = "The sum of 2 and 7 is 9; index_1 = 1 and index_2 = 2; thus [1,2]"
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        numbers = [2,3,4]
        target = 6
        actual = Solution.twoSum(numbers, target)
        expected = [1,3]
        msg = "The sum of 2 and 4 is 6; index_1 = 1 and index_2 = 3; thus [1,3]"
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        numbers = [-1,0]
        target = -1
        actual = Solution.twoSum(numbers, target)
        expected = [1,2]
        msg = "The sum of -1 and 0 is -1; index_1 = 1 and index_2 = 2; thus [1,2]"
        self.assertEqual(actual, expected, msg)
