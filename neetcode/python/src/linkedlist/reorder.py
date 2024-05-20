from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def reorderList(self, head: ListNode)-> None:
        # get a pointer to the middle of the list, in "slow"
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # create a separate, second list of the upper nodes reversed, in "prev"
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        # connect the lower portion of the list with the upper portion:
        # lower_i -> upper_i -> lower_i+1
        lower, upper = head, prev
        while upper:
            lowerTemp, upperTemp = lower.next, upper.next
            lower.next = upper
            upper.next = lowerTemp
            lower, upper = lowerTemp, upperTemp

    # stack-based solution
    def reorderListStack(self, head: ListNode) -> None:
        # get a pointer to the middle of the list, in "slow"
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # push upper half of list into a stack
        st = []
        slow = slow.next
        while slow:
            st.append(slow)
            slow = slow.next

        # attach nodes from stack
        front = head
        while st:
            back = st.pop()
            temp = front.next
            front.next = back
            back.next = temp
            front = temp
        front.next = None
