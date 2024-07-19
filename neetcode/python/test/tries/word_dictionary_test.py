import unittest
from src.tries.word_dictionary import WordDictionary

class WordDictionaryTest(unittest.TestCase):
    def test_init(self):
        wd = WordDictionary()
        self.assertTrue(True)

    def test_example1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")

        a = wordDictionary.search("pad")    # return False
        self.assertFalse(a)
        b = wordDictionary.search("bad")    # return True
        self.assertTrue(b)
        c = wordDictionary.search(".ad")    # return True
        self.assertTrue(c)
        d = wordDictionary.search("b..")    # return True
        self.assertTrue(d)

    def test_example2(self):
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("a")

        a = wd.search(".")
        self.assertTrue(a)

        b = wd.search("a")
        self.assertTrue(b)

        c = wd.search("aa")
        self.assertFalse(c)

        d = wd.search("a")
        self.assertTrue(d)

        e = wd.search(".a")
        self.assertFalse(e)

        f = wd.search("a.")
        self.assertFalse(f)
