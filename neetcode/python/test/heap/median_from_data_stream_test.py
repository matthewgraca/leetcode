import unittest
import heapq
from src.heap.median_from_data_stream import MedianFinder

class MedianFromDataStreamTest(unittest.TestCase):
    def test_init(self):
        mf = MedianFinder()
        self.assertTrue(True)

    def test_findMedian_single_input(self):
        mf = MedianFinder()
        datastream = [0]
        for data in datastream:
            mf.addNum(data)

        actual = mf.findMedian()
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_findMedian_odd_input(self):
        mf = MedianFinder()
        datastream = [0,5,1]
        for data in datastream:
            mf.addNum(data)

        actual = mf.findMedian()
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_findMedian_even_input(self):
        mf = MedianFinder()
        datastream = [0,5,1,10]
        for data in datastream:
            mf.addNum(data)

        actual = mf.findMedian()
        expected = 3.0
        self.assertEqual(actual, expected)

    def test_example1(self):
        medianFinder = MedianFinder()
        medianFinder.addNum(1)    # arr = [1]
        medianFinder.addNum(2)    # arr = [1, 2]
        actual1 = medianFinder.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
        expected1 = 1.5
        self.assertEqual(actual1, expected1)

        medianFinder.addNum(3)    # arr[1, 2, 3]
        actual2 = medianFinder.findMedian() # return 2.0
        expected2 = 2.0
        self.assertEqual(actual2, expected2)
