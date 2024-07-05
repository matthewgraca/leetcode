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
        heapq.heappush(self.minheap, val)
        # if there are more than k items, pop the smallest items
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0] 
