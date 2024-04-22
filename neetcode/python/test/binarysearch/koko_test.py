import unittest
from src.binarysearch.koko import Solution

class KokoTest(unittest.TestCase):
    def test_example1(self):
        piles = [3,6,7,11]
        h = 8
        actual = Solution().minEatingSpeed(piles, h)
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        piles = [30,11,23,4,20]
        h = 5
        actual = Solution().minEatingSpeed(piles, h)
        expected = 30
        self.assertEqual(actual, expected)
        
    def test_example3(self):
        piles = [30,11,23,4,20]
        h = 6
        actual = Solution().minEatingSpeed(piles, h)
        expected = 23
        self.assertEqual(actual, expected)

    def test_example4(self):
        piles = [312884470]
        h = 312884469
        actual = Solution().minEatingSpeed(piles, h)
        expected = 2
        self.assertEqual(actual, expected)
