import unittest
from src.linkedlist.merge_two import Solution
from src.linkedlist.ListNode import ListNode

class MergeTwoTest(unittest.TestCase):
    def test_example1(self):
        list1 = [1,2,4]
        list2 = [1,3,4]

        # convert input to linked lists 
        l1 = ListNode().linkedListOf(list1)
        l2 = ListNode().linkedListOf(list2)
        actual = Solution().mergeTwoLists(l1, l2)

        # convert ouput to list for checking
        actualList = ListNode().listOf(actual)
        expected = [1,1,2,3,4,4]

        self.assertEqual(actualList, expected)
