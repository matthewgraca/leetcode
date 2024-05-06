from src.linkedlist.ListNode import ListNode
from typing import List
import heapq

class Solution:
    def __init__(self):
        pass

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # lists are fully merged if only one remains
        while len(lists) > 1:
            # merge lists by pairs
            mergedSubLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # skip l2 for odd number of lists
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedSubLists.append(self.merge(l1, l2))
            lists = mergedSubLists

        # handle empty list case
        return lists[0] if lists else None 

    def mergeKListsNaiveMerge(self, lists: List[ListNode]) -> ListNode:
        head = temp = ListNode(float('-inf'))
        # get list, merge with previous list
        for l in lists:
            head = self.merge(head, l)
        return head.next 

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # if one list is depleted, take all from the other
        tail.next = l1 if l1 else l2 
        return head.next

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

    def mergeKListsSort(self, lists: List[ListNode]) -> ListNode:
        # iterate through each node and push into a list 
        res = []
        for nodelist in lists:
            temp = nodelist
            while temp:
                res.append(temp.val)
                temp = temp.next

        # sort the list and convert to list of nodes
        head = temp = ListNode(0)
        res.sort()
        for val in res:
            temp.next = ListNode(val)
            temp = temp.next
        return head.next 
'''
let k be the number of lists, m be the amount of items per list, and m*k be the total amount of items, abbreviated to n
option 0: merge each list
1. get a list, merge with next list
- O(mk^2) = O(kn)
    - for every list (k), we merge O(m) items
    - m+m + 2m+m + 3m+m + ... + (k-1)m+m
    - = (1m + 2m + ... (k-1)m) + (m + m + ... m)
    - = m(1 + 2 + .. + k-1) + km
    - = m(((k-1)/2)(k)) + km
    - == mk^2
- O(1)
    - simple stitching nodes

option 1: just sort lol
1. put every val into a list
2. sort the list
3. convert into list of nodes
- O(mklog(mk)) = O(nlogn)
    - mklog(mk) for sort
    - mk for creating a list of nodes
- O(mk) = O(n)
    - mk space for new list of nodes
    - not sure why is this less space efficient when ran on leetcode than the heap
        solution. res.sort() is in-place (vs sorted(res))

option 2: heap
1. put every head value into a heap (heap of lists)
2. pop the smallest value
3. push the new head of the list that got popped back into the heap
- O(mklogk) = O(nlogk)
    - heap only contain k values (k lists), push/pop (lgk) is called mk times
    - mk time to create new list of nodes
- O(k)
    - k space for the heap

option 3: mergesort 
another way is to reinterpret how you do your mergesort. instead of merging that requires k*n 
compares, you can merge each list together, two at a time
(that is, merge 1->2, 3->4, ... k-1->k. each merge takes n time. then we merge 1&2->3&4 ..., 
which occurs logk times)
(compare this to option 0; folding 1->2=1, then 1->3=1, then 1->k. each merge is n times,
so for k lists that nk time)

1. get a list, merge with next list
2. continue until one list remains
- O(mklogk) = O(nlogk)
    - m+m + m+m + ... m+m + 2m+2m + ... + 2m+2m + 4m+4m + ... + 4m+4m ... m(k/2) + m(k/2) = 
    - = km + (k/2)2m + ... + (k/k)km
    - = km + km + km + ... + km
    - each iteration, k halves until it reaches 1; so there are logk terms
    - = km*logk
- O(1): just stitching references together
- only advantage is it's parallelizable. the heap is preferable in terms of ease
'''
