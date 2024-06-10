import unittest
from src.heap.last_stone_weight import Solution

class LastStoneWeightTest(unittest.TestCase):
    def test_example1(self):
        stones = [2,7,4,1,8,1]
        actual = Solution().lastStoneWeight(stones)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example2(self):
        stones = [1]
        actual = Solution().lastStoneWeight(stones)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example3_no_stone_remains(self):
        stones = [4,4]
        actual = Solution().lastStoneWeight(stones)
        expected = 0
        self.assertEqual(actual, expected)
