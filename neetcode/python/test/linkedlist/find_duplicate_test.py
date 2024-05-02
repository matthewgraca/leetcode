import unittest
from src.linkedlist.find_duplicate import Solution

class FindDuplicateTest(unittest.TestCase):
    def test_example1(self):
        nums = [1,3,4,2,2]
        actual = Solution().findDuplicate(nums)
        expected = 2
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [3,1,3,4,2]
        actual = Solution().findDuplicate(nums)
        expected = 3
        self.assertEqual(actual, expected)

    def test_example3(self):
        nums = [3,3,3,3,3]
        actual = Solution().findDuplicate(nums)
        expected = 3
        self.assertEqual(actual, expected)

    def test_example4(self):
        nums = [1,3,4,2,1]
        actual = Solution().findDuplicate(nums)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example4(self):
        nums = [4,3,1,4,2]
        actual = Solution().findDuplicate(nums)
        expected = 4
        self.assertEqual(actual, expected)

