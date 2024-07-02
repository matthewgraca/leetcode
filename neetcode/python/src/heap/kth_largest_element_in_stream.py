from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # create a heap of the nums list
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)

        # kick out the bottom k items, so the top k items remain
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # if there are less than k items, just freely add val
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        # if there are k items but the val belongs in the top k, push it and pop the k+1th item
        elif self.minheap[0] < val:
            heapq.heappushpop(self.minheap, val)
        # else the heap is full and val is in the bottom k; just ignore it

        return self.minheap[0] 
