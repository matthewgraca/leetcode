import unittest
from src.binarysearch.tbkvs import TimeMap

class TBKVSTest(unittest.TestCase):
    def test_init(self):
        constructor = TimeMap()
        self.assertTrue(True)

    def test_setAndGet1_setIntoGet(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        actual = tm.get("foo", 1)
        expected = "bar"
        self.assertEqual(actual, expected)

    def test_setAndGet2_getWithValidKeyButInvalidTimestamp(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        actual = tm.get("foo", 3)
        # should return the value at the key, with the largest previous timestamp
        expected = "bar"
        self.assertEqual(actual, expected)

    def test_setAndGet3_setSameKeyNewValue(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        tm.set("foo", "bar2", 4)
        actual = tm.get("foo", 4)
        expected = "bar2"
        self.assertEqual(actual, expected)

    def test_setAndGet4_getValidKeyInvalidTimestamp(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        tm.set("foo", "bar2", 4)
        actual = tm.get("foo", 5)
        expected = "bar2"
        self.assertEqual(actual, expected)

    def test_setAndGet5_getOlderValue(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        tm.set("foo", "bar2", 4)
        actual = tm.get("foo", 1)
        expected = "bar"
        self.assertEqual(actual, expected)

    def test_49TestCase_set1(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        actual = tm.get("love", 10)
        expected = "high"
        self.assertEqual(actual, expected)

    def test_49TestCase_set2(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        tm.set("love", "low", 20)
        actual = tm.get("love", 20)
        expected = "low"
        self.assertEqual(actual, expected)

    def test_49TestCase_get1(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        tm.set("love", "low", 20)
        actual = tm.get("love", 5)
        expected = ""
        self.assertEqual(actual, expected)

    def test_49TestCase_get2(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        tm.set("love", "low", 20)
        actual = tm.get("love", 10)
        expected = "high"
        self.assertEqual(actual, expected)

    def test_49TestCase_get3(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        tm.set("love", "low", 20)
        actual = tm.get("love", 15)
        expected = "high"
        self.assertEqual(actual, expected)

