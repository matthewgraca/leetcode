from src.linkedlist.ListNode import ListNode 

class Solution:
    def __init__(self):
        pass

    # no stack, single pass, slow-fast ptr solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    # stack-based, iterative solution
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        # create a stack that contains all nodes
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        # pop n items from stack; curr will have nth node from the end
        curr = None
        for i in range(n):
            curr = stack.pop()

        # top of stack has previous node
        if stack:
            prev = stack[-1]
            prev.next = curr.next
        else:
            head = head.next

        return head
