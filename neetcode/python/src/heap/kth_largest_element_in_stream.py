from typing import List
from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapify(self.minHeap)

        # prune values lower than kth s.t. the top val is the kth largest
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        # ensure the top value is the kth largest
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

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

    heappushpop() is nice because:
        - if the val is less than or equal to kth, it gets pushed to the top 
            and immediately popped.
        - if the val is greater than kth, it gets pushed and the now k+1th
            value gets popped, and the kth value rises to the top.
        - unfortunately, we cant use it because add() may be called when 
            there aren't even enough items in the list to begin with. 
            if len(heap) < k and heappushpop() is called, it will potentially
            get rid of the kth value and add a duplicate val.
            - so just push the val, then pop if it grows too large

time: 
    - heapifying an existing list takes n time
    - we pop n-k items from the heap; taking (n-k)log(n?) time
    - in total, initialization costs about nlogn time
    - as for add(), the heap is size k and each call of push and pop takes logk time.
        - 2logk per call
space:
    - we create a heap of size n that gets trimmed down to size k: so total size is n
    - add only uses constant space 1
'''
