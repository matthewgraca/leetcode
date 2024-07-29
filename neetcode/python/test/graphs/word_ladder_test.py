import unittest
from src.graphs.word_ladder import Solution

class WordLadderTest(unittest.TestCase):
    def test_example1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        actual = Solution().ladderLength(beginWord, endWord, wordList)
        expected = 5
        self.assertEqual(actual, expected)

    def test_example2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        actual = Solution().ladderLength(beginWord, endWord, wordList)
        expected = 0
        self.assertEqual(actual, expected)

    def test_example3(self):
        beginWord = "a"
        endWord = "c"
        wordList = ["a","b","c"]
        actual = Solution().ladderLength(beginWord, endWord, wordList)
        expected = 2
        self.assertEqual(actual, expected)

    def test_example4(self):
        beginWord = "hot"
        endWord = "dog"
        wordList = ["hot","dog"]
        actual = Solution().ladderLength(beginWord, endWord, wordList)
        expected = 0
        self.assertEqual(actual, expected)
