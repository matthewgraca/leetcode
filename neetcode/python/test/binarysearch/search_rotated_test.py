import unittest
from src.binarysearch.search_rotated import Solution

class SearchRotatedTest(unittest.TestCase):
    def test_example1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        actual = Solution().search(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        actual = Solution().search(nums, target)
        expected = -1
        self.assertEqual(actual, expected)

    def test_example3(self):
        nums = [1]
        target = 0
        actual = Solution().search(nums, target)
        expected = -1
        self.assertEqual(actual, expected)

    def test_nonRotatedAndTargetDoesntExist(self):
        nums = [1,2,3,4,5,6]
        target = 0
        actual = Solution().search(nums, target)
        expected = -1
        self.assertEqual(actual, expected)

    def test_nonRotatedAndTargetExists(self):
        nums = [1,2,3,4,5,6]
        target = 3
        actual = Solution().search(nums, target)
        expected = 2
        self.assertEqual(actual, expected)

    def test_example4(self):
        nums = [3,5,1]
        target = 3
        actual = Solution().search(nums, target)
        expected = 0
        self.assertEqual(actual, expected)
