from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseList(head, k, k)

    # scans ahead to check if a valid k-group exists
    def kGroupFound(self, curr: ListNode, k: int) -> ListNode:
        count = 1
        temp = curr
        while temp.next and count < k:
            temp = temp.next
            count += 1
        return True if count == k else False

    def reverseList(self, head: ListNode, count: int, k: int) -> ListNode:
        # base case: invalid k-group
        # if no valid k-group is ahead, do not reverse
        if not self.kGroupFound(head, k):
            return head

        # reverse current k-group
        prev = None
        curr = head
        after = None
        while curr and count > 0:
            after = curr.next
            curr.next = prev
            prev = curr 
            curr = after
            count -= 1

        # if there's another possible k-group, recurse
        if after:
            head.next = self.reverseList(after, k, k)

        return prev

