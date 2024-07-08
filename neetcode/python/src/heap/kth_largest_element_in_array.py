from typing import List
import random
import heapq

class Solution:
    def __init__(self):
        pass

    # djikstra's dutch flag quickselect (i.e. 3-way quickselect paritioning)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # choose pivot and construct left, mid, right partitions
        # just making the paritions instead of indexing since indexing is a pain
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        
        # if k exists in the left partition, go left
        if len(left) >= k:
            return self.findKthLargest(left,k)
        # if k exists in the right partition, go right
        if len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        # if k is in the middle partition, kth has been found
        return pivot

    
    # heap solution
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return minheap[0]
