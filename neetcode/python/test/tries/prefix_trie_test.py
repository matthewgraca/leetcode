import unittest
from src.tries.prefix_trie import Trie

class PrefixTrieTest(unittest.TestCase):
    def test_init(self):
        trie = Trie()
        self.assertTrue(True)

    def test_searchEmptyTrie(self):
        trie = Trie()
        self.assertFalse(trie.search("string"))

    def test_insertOneItem(self):
        trie = Trie()
        trie.insert("a")
        self.assertTrue(trie.search("a"))

    def test_insertManyItems(self):
        trie = Trie()
        trie.insert("abc")
        self.assertTrue(trie.search("abc"))

    def test_wordInPathButNotInTrieReturnsFalse(self):
        trie = Trie()
        trie.insert("abc")
        self.assertFalse(trie.search("ab"))

    def test_prefixOfWord(self):
        trie = Trie()
        trie.insert("abc")
        self.assertTrue(trie.startsWith("ab"))

    def test_prefixIsSameWord(self):
        trie = Trie()
        trie.insert("abc")
        self.assertTrue(trie.startsWith("abc"))

    def test_insertTwoWordsOnSamePath(self):
        trie = Trie()
        trie.insert("app")
        trie.insert("apps")
        self.assertTrue(trie.search("app") and trie.search("apps"))

    def test_example1(self):
        trie = Trie()
        trie.insert("apple")

        a = trie.search("apple")   # return True
        self.assertTrue(a)

        b = trie.search("app")     # return False
        self.assertFalse(b)

        c = trie.startsWith("app") # return True
        self.assertTrue(c)

        trie.insert("app")
        d = trie.search("app")     # return True
        self.assertTrue(d)
