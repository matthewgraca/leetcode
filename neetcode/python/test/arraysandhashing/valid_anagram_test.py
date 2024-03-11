import unittest
from src.arraysandhashing.valid_anagram import Solution

class ValidAnagramTest(unittest.TestCase):
    def test_example1(self):
        arg1 = "anagram"
        arg2 = "nagaram"
        actual = Solution.isAnagram(arg1, arg2)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        arg1 = "rat"
        arg2 = "car"
        actual = Solution.isAnagram(arg1, arg2)
        expected = False 
        self.assertEqual(actual, expected)
