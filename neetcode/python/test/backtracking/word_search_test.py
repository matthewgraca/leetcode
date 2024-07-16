import unittest
from src.backtracking.word_search import Solution

class WordSearchTest(unittest.TestCase):
    def test_example1(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCCED"
        actual = Solution().exist(board, word)
        expected = True
        self.assertTrue(actual, expected)
