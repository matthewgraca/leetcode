import unittest
from src.linkedlist.ListNode import ListNode
from src.linkedlist.reverse_nodes_in_k_group import Solution

class ReverseNodesInKGroupTest(unittest.TestCase):
    def test_example1(self):
        head = ListNode().linkedListOf([1,2,3,4,5])
        k = 2
        actual = ListNode().listOf(Solution().reverseKGroup(head, k))
        expected = [2,1,4,3,5]
        self.assertEqual(actual, expected)

    def test_example2(self):
        head = ListNode().linkedListOf([1,2,3,4,5])
        k = 3
        actual = ListNode().listOf(Solution().reverseKGroup(head, k))
        expected = [3,2,1,4,5]
        self.assertEqual(actual, expected)
