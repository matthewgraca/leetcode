from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after 

        return prev 
