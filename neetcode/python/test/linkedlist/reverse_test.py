import unittest
from src.linkedlist.reverse import Solution
from src.linkedlist.ListNode import ListNode

class ReverseTest(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        actualArr = []
        actual = Solution().reverseList(head)
        temp = actual 
        while temp:
           actualArr.append(temp.val)
           temp = temp.next

        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None)))))
        expectedArr = [5,4,3,2,1]

        self.assertEqual(actualArr, expectedArr)
