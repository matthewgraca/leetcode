import unittest
from src.arraysandhashing.group_anagrams import Solution

class GroupAnagramsTest(unittest.TestCase):
    def test_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        actual = Solution.groupAnagrams(strs)
        for s in actual:
            s.sort()
        actual.sort()
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        for s in expected:
            s.sort()
        expected.sort()
        self.assertEqual(actual, expected)

    def test_example2(self):
        strs = [""]
        actual = Solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(actual, expected)

    def test_example3(self):
        strs = ["a"]
        actual = Solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(actual, expected)
