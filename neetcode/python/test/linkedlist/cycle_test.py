import unittest
from src.linkedlist.cycle import Solution
from src.linkedlist.ListNode import ListNode

class CycleTest(unittest.TestCase):
    def test_example1(self):
        l = [ListNode(3),ListNode(2),ListNode(0),ListNode(-4)]
        pos = 1
        l[0].next = l[1]
        l[1].next = l[2]
        l[2].next = l[3]
        l[3].next = l[pos]

        head = l[0]
        actual = Solution().hasCycle(head)
        expected = True
        self.assertEqual(actual, expected)
        
    def test_example2(self):
        l = [ListNode(1),ListNode(2)]
        pos = 0
        l[0].next = l[1]
        l[1].next = l[pos]

        head = l[0]
        actual = Solution().hasCycle(head)
        expected = True
        self.assertEqual(actual, expected)
                
    def test_example3(self):
        l = [ListNode(1)]

        head = l[0]
        actual = Solution().hasCycle(head)
        expected = False 
        self.assertEqual(actual, expected)
 
    def test_example4(self):
        l = []
        head = None
        actual = Solution().hasCycle(head)
        expected = False
        self.assertEqual(actual, expected)
