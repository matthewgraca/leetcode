from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    '''
    l0, l1, l2, ... ln-1, ln
    l0, ln, l1, ln-1, l2, ln-2, ...
    '''
    # recursive solution
    # using terms from clrs book instead of (base, recursive step) 
    def reorderListR(self, head: ListNode) -> None:
        self.recursiveReorder(head, head)

    def recursiveReorder(self, mid: ListNode, right: ListNode) -> ListNode:
        # conquer 
        if right.next == None:
            return right
        if right.next.next == None:
            return right.next
        # divide
        # returns the right value at the end of the list
        right = self.recursiveReorder(mid.next, right.next.next)
        # combine
        
    # iterative, non-stack based solution
    def reorderList(self, head: ListNode) -> None:
        # split the list in two, demarcated by the left pointer
        left, right = head, head.next
        while right and right.next:
            left = left.next
            right = right.next.next

        # reverse the upper half of the list
        # taken from Reverse Linked List problem
        upper = left.next
        prev = left.next = None
        while upper:
            temp = upper.next
            upper.next = prev
            prev = upper 
            upper = temp

        # attach each node from lower list to upper list
        # lower -> lower list, upper -> upper list
        lower, upper = head, prev
        while upper:
            lowertmp, uppertmp = lower.next, upper.next
            lower.next = upper
            upper.next = lowertmp 
            lower, upper = lowertmp, uppertmp 
            
    # iterative, stack-based solution
    def reorderListIt(self, head: ListNode) -> None:
        # traverse list, where the right pointer points to the final node
        # and the mid pointer points to the middle node (ceiling(n/2))
        # done by moving right twice while moving mid once per iteration 
        mid = right = left = head
        while right.next != None:
            mid = mid.next
            # prevent right from going past the end
            if right.next.next == None:
                right = right.next
            else:
                right = right.next.next

        # push all node pointers from mid to end into a stack
        stack = []
        while mid:
            stack.append(mid)
            mid = mid.next

        # reattach
        temp = head
        while temp.next:
            temp = temp.next
            right = stack.pop()
            left.next = right 
            right.next = temp
            left = temp 
            if temp.next == right:
                temp.next = None

'''
not even gonna attempt the recursive version

biggest idea is two pointers -- slow and fast, where fast goes 2x slow so slow ends up in the middle

the trick is that you can reverse the second half, then attach nodes iteratively
o(n) time, no space
'''
