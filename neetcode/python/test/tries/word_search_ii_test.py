import unittest
from src.tries.word_search_ii import Solution

class WordSearchIITest(unittest.TestCase):
    def test_example1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        actual = Solution().findWords(board, words)
        expected = ["eat","oath"]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        actual = Solution().findWords(board, words)
        expected = []
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example3(self):
        board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
        words = ["oa", "oaa"]
        actual = Solution().findWords(board, words)
        expected = ["oa", "oaa"]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example4(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
        actual = Solution().findWords(board, words)
        expected = ["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"]
        self.assertEqual(sorted(actual), sorted(expected))

