import unittest
from src.heap.kth_largest_element_in_stream import KthLargest

class KthLargestElementInStream(unittest.TestCase):
    def test_init_successfully_compiles(self):
        klargest = KthLargest(0, list())
        self.assertTrue(True)

    # k = 2, adding -1 doesn't change k
    def test_add_item_smaller_than_k(self):
        klargest = KthLargest(4, [0,1,2,3,4,5])
        actual = klargest.add(-1)
        expected = 2
        self.assertEqual(actual, expected)

    # k = 2, adding 6 makes k = 3
    def test_add_item_larger_than_k(self):
        klargest = KthLargest(4, [0,1,2,3,4,5])
        actual = klargest.add(6)
        expected = 3
        self.assertEqual(actual, expected)

    # k = 2, adding 3 makes k = 3
    def test_add_item_at_k(self):
        klargest = KthLargest(4, [0,1,2,4,5,6])
        actual = klargest.add(3)
        expected = 3
        self.assertEqual(actual, expected)

    # add is guaranteed to be used at a valid k
    def test_k_greater_than_nums_len(self):
        klargest = KthLargest(1, [])
        actual = klargest.add(3)
        expected = 3
        self.assertEqual(actual, expected)
