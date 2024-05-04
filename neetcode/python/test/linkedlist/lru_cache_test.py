import unittest
from src.linkedlist.lru_cache import LRUCache

class LRUCacheTest(unittest.TestCase):
    def test_0_init(self):
        cache = LRUCache(1)
        self.assertTrue(True)

    def test_1_getEmptyFails(self):
        cache = LRUCache(1)
        actual = cache.get(7)
        expected = -1
        self.assertEqual(actual, expected)

    def test_2_put(self):
        cache = LRUCache(1)
        cache.put(1, 100)
        self.assertTrue(True)

    def test_3_getValueThatWasntPutFails(self):
        cache = LRUCache(1)
        cache.put(1, 100)
        actual = cache.get(7)
        expected = -1
        self.assertEqual(actual, expected)

    def test_4_getValueThatWasPutSucceeds(self):
        cache = LRUCache(1)
        cache.put(1, 100)
        actual = cache.get(1)
        expected = 100
        self.assertEqual(actual, expected)

    # this point on assumes get() is working. 
    # if get() is bad, upper tests should fail
    def test_5_putFillsCache(self):
        cache = LRUCache(3)
        cache.put(1,100)
        cache.put(2,200)
        cache.put(3,300)
        actual = [cache.get(1), cache.get(2), cache.get(3)]
        expected = [100, 200, 300]
        self.assertEqual(actual, expected)

    def test_6_putEvictsWhenCacheIsFull(self):
        cache = LRUCache(1)
        cache.put(1, 100)
        cache.put(2, 300)
        actual = cache.get(1)
        expected = -1
        self.assertEqual(actual, expected)

    # leetcode test cases
    def test_7_leetcode_case_7(self):
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(2, 2)
        actual = cache.get(2)
        expected = 2
        self.assertEqual(actual, expected)

        cache.put(1,1)
        cache.put(4,1)
        actual = cache.get(2)
        expected = -1
        self.assertEqual(actual, expected)
