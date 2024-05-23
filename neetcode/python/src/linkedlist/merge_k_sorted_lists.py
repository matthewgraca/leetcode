from src.linkedlist.ListNode import ListNode
from typing import List
import heapq

class Solution:
    def __init__(self):
        pass

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # divide and conquer merge:
        # merge each sublist with each other in pairs; 
        # doubling the size of each list, but halving the number of lists
        # at each iteration. continue until one list remains.
        
        # merge lists until one remains
        while len(lists) > 1:
            # merge sublists in pairs
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedlists.append(self.merge(l1, l2))
            lists = mergedlists
        
        # if given empty list, return null
        return lists[0] if lists else None

    # merges l1 into l2, ascending order
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        
        return dummy.next

    def mergeKListsHeap(self, lists: List[ListNode]) -> ListNode:
        res = temp = ListNode(0)
        h = []
        heapq.heapify(h)

        # put every head into the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))

        while h:
            # pop the smallest head, add to result
            val, idx = heapq.heappop(h)
            temp.next = lists[idx]
            temp = temp.next

            # if the list we popped has another item, push it 
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(h, (lists[idx].val, idx))

        return res.next 
