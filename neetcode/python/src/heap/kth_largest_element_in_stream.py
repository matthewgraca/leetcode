from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # prune values lower than kth s.t. the top val is the kth largest
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # ensure the top value is the kth largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] 
'''
idea:
    convert nums to a max heap
    each addition pops k items (returning the kth largest)
        after popping k items, we add those items + val back into the heap
            -- i don't like this popping + readding, though

trick:
    we're not removing any values; we only need to remember the values 
    that are larger than the kth largest; any values that we come across
    that are smaller than that can just go to the trash

    heapq.heappushpop() is nice because:
        - if the val is less than or equal to kth, it gets pushed to the top 
            and immediately popped.
        - if the val is greater than kth, it gets pushed and the now k+1th
            value gets popped, and the kth value rises to the top.
        - unfortunately, we cant use it because add() may be called when 
            there aren't even enough items in the list to begin with. 
            if len(heap) < k and heappushpop() is called, it will potentially
            get rid of the kth value and add a duplicate val.
            - so just push the val, then pop if it grows too large

'''
