import unittest
from src.linkedlist.ListNode import ListNode 
from src.linkedlist.remove_nth_node import Solution

class RemoveNthNodeTest(unittest.TestCase):
    def test_example1(self):
        ln = ListNode()
        head = ln.linkedListOf([1,2,3,4,5])
        n = 2
        actual = ln.listOf(Solution().removeNthFromEnd(head, n))
        expected = [1,2,3,5]
        self.assertEqual(actual, expected)

    def test_example2(self):
        ln = ListNode()
        head = ln.linkedListOf([1])
        n = 1
        actual = ln.listOf(Solution().removeNthFromEnd(head, n))
        expected = []
        self.assertEqual(actual, expected)
        
    def test_example3(self):
        ln = ListNode()
        head = ln.linkedListOf([1,2])
        n = 1
        actual = ln.listOf(Solution().removeNthFromEnd(head, n))
        expected = [1]
        self.assertEqual(actual, expected)

    def test_example4(self):
        ln = ListNode()
        head = ln.linkedListOf([1,2])
        n = 2
        actual = ln.listOf(Solution().removeNthFromEnd(head, n))
        expected = [2]
        self.assertEqual(actual, expected)
