from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    # same as iterative solution, just done recursively
    def reverseList(self, head: ListNode) -> ListNode:
        # base case 1: empty list
        if head == None:
            return None 
        # base case 2: list of 1 item; trivially reversed
        if head.next == None:
            return head 

        # recursive case: keep calling until two nodes remain
        # repeatedly update newHead to be the last node of the list 
        newHead = self.reverseList(head.next) 
        # due to recursion, we never lose the previous node
        # swap two nodes
        head.next.next = head
        head.next = None
        return newHead 


    # iterates through list and reverse pointers
    def reverseListIter(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        return prev 

    # iterates through list and generates result as if it were a stack 
    def reverseListExpensive(self, head: ListNode) -> ListNode:
        res = None
        temp = head
        while temp:
            node = ListNode(temp.val, res)
            res = node
            temp = temp.next
        
        return res 
