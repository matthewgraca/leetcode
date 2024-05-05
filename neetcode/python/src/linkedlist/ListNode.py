from typing import List

class ListNode:
    class ListNode:
        pass

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # takes a list and converts it into a linked list
    def linkedListOf(self, arr: List[int]) -> ListNode:
        head = temp = ListNode(0)
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
        return head.next
    
    # takes a linked list and converts it into a list
    def listOf(self, head: ListNode):
        temp = head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res
