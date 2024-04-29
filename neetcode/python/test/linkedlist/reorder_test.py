import unittest
from src.linkedlist.reorder import Solution
from src.linkedlist.ListNode import ListNode

class ReorderTest(unittest.TestCase):
    def test_evenInput(self):
        head = [1,2,3,4]
        actual = ListNode().linkedListOf(head)
        Solution().reorderList(actual)
        actualList = ListNode().listOf(actual)
        expectedList = [1,4,2,3]
        self.assertEqual(actualList, expectedList)

    def test_oddInput(self):
        head = [1,2,3,4,5]
        actual = ListNode().linkedListOf(head)
        Solution().reorderList(actual)
        actualList = ListNode().listOf(actual)
        expectedList = [1,5,2,4,3]
        self.assertEqual(actualList, expectedList)


