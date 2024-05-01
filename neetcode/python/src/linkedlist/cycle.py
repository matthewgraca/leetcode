from src.linkedlist.ListNode import ListNode 

class Solution:
    def __init__(self):
        pass

    def hasCycle(self, head: ListNode) -> bool:
        # empty list implies no cycle
        if head is None:
            return False

        slow, fast = head, head.next
        while fast:
            # fast catches slow implies cycle
            if fast is slow:
                return True
            # fast hits null implies no cycle
            if fast.next is None:
                return False 
            # move ptrs; keep fast at 2x speed of slow
            slow = slow.next
            fast = fast.next.next
        # if this is reached, fast hit null; implies no cycle
        return False

    # stuff every node into a set. if the next node points to a node in the set, there's a cycle
    def hasCycleSet(self, head: ListNode) -> bool:
        # if there's no cycle, temp will eventually be null
        # if there's a cycle, we'll eventually hit a dupe, returning true 
        nodes = set()
        temp = head
        while temp:
            if temp in nodes:
                return True 
            else:
                nodes.add(temp)
                temp = temp.next
        return False 
