from src.linkedlist.ListNode import ListNode 

class Solution:
    def __init__(self):
        pass

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # have slow be 1 slower than fast
        dummy = ListNode(-1, head)
        slow, fast = dummy, head

        # move fast to nth from beginning
        while n > 0:
            fast = fast.next
            n -= 1
        
        # move slow until fast hits end of list
        # slow will be n+1 from the end
        while fast:
            slow, fast = slow.next, fast.next
        
        # connect
        slow.next = slow.next.next

        return dummy.next
