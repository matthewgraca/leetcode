import unittest
from src.linkedlist.ListNode import ListNode
from src.linkedlist.add_two import Solution

class AddTwoTest(unittest.TestCase):
    def test_example1(self):
        l1, l2 = [2,4,3], [5,6,4]
        ln = ListNode()
        actual = ln.listOf(
                    Solution().addTwoNumbers(
                            ln.linkedListOf(l1), ln.linkedListOf(l2)
                        )
                    )
        expected = [7,0,8]
        self.assertEqual(actual, expected)

    def test_example2(self):
        l1, l2 = [0], [0]
        ln = ListNode()
        actual = ln.listOf(
                    Solution().addTwoNumbers(
                            ln.linkedListOf(l1), ln.linkedListOf(l2)
                        )
                    )
        expected = [0]
        self.assertEqual(actual, expected)

    def test_example3(self):
        l1, l2 = [9,9,9,9,9,9,9], [9,9,9,9]
        ln = ListNode()
        actual = ln.listOf(
                    Solution().addTwoNumbers(
                            ln.linkedListOf(l1), ln.linkedListOf(l2)
                        )
                    )
        expected = [8,9,9,9,0,0,0,1]
        self.assertEqual(actual, expected)

    def test_example4(self):
        l1, l2 = [2,4,9], [5,6,4,9]
        ln = ListNode()
        actual = ln.listOf(
                    Solution().addTwoNumbers(
                            ln.linkedListOf(l1), ln.linkedListOf(l2)
                        )
                    )
        expected = [7,0,4,0,1]
        self.assertEqual(actual, expected)
