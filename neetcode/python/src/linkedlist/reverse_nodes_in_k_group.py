from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseGroup(head, k, k)
    
    # recursively reverses every k-group in the list
    def reverseGroup(self, head: ListNode, count: int, k: int) -> ListNode:
        # base case: no k-group, return
        if not self.validKGroup(head, k):
            return head

        # recursive step: 
        # 1. reverse the current group,
        prev, curr, after = None, head, None
        while count:
            after = curr.next
            curr.next = prev
            prev, curr = curr, after
            count -= 1

        # 2. then reverse the next k-group 
        if after:
            head.next = self.reverseGroup(after, k, k)
        
        # once all lists reversed, return the head of the original reversed list
        return prev

    # checks if the given list has a valid k-group
    def validKGroup(self, head: ListNode, k: int) -> bool:
        temp = head
        while temp and k:
            temp = temp.next
            k -= 1
        # if the list ends before k hits 0, this is an invalid k-group
        return True if k == 0 else False
