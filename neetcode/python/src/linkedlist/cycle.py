from src.linkedlist.ListNode import ListNode 

class Solution:
    def __init__(self):
        pass

    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        # if the fast pointer catches the slow pointer, a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
