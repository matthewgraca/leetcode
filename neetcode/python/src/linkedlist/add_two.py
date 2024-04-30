from src.linkedlist.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = l1, l2
        head = temp3 = ListNode(0)
        carry = 0
        while temp1 or temp2 or carry:
            # grab values from both lists
            op1, op2 = 0, 0
            if temp1:
                op1 = temp1.val
                temp1 = temp1.next
            if temp2:
                op2 = temp2.val
                temp2 = temp2.next

            # add 
            val = op1 + op2 + carry
            temp3.next = ListNode(val % 10)
            carry = val  // 10
            temp3 = temp3.next

        return head.next
