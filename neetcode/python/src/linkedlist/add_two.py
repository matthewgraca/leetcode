from src.linkedlist.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = temp = ListNode(-1)
        carry = 0

        # take from l1 and l2
        while l1 or l2 or carry:
            # pull values from l1 and/or l2
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            
            # perform sum
            sumval = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            temp.next = ListNode(sumval)
            temp = temp.next

        return dummy.next   
