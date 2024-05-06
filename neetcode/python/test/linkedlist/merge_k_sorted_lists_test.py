import unittest
from src.linkedlist.merge_k_sorted_lists import Solution
from src.linkedlist.ListNode import ListNode

class MergeKSortedLists(unittest.TestCase):
    def test_example1(self):
        lists = [[1,4,5],[1,3,4],[2,6]]
        llists = []
        for i in lists:
            llists.append(ListNode().linkedListOf(i))
        actual = ListNode().listOf(Solution().mergeKLists(llists))
        expected = [1,1,2,3,4,4,5,6]
        self.assertEqual(actual, expected)

    def test_example2(self):
        lists = []
        llists = []
        for i in lists:
            llists.append(ListNode().linkedListOf(i))
        actual = ListNode().listOf(Solution().mergeKLists(llists))
        expected = []
        self.assertEqual(actual, expected)

    def test_example3(self):
        lists = [[]]
        llists = []
        for i in lists:
            llists.append(ListNode().linkedListOf(i))
        actual = ListNode().listOf(Solution().mergeKLists(llists))
        expected = []
        self.assertEqual(actual, expected)
