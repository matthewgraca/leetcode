import random
from heapq import *
from typing import List

class Solution:
    def __init__(self):
        pass

    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthLargest = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while True:
            # random pivots protect against worst case
            randPivot = random.randint(lo, hi)
            pivot = self.partition(nums, lo, hi, randPivot)

            # move to the subarray that has the kth largest value
            if pivot == kthLargest:
                return nums[pivot]
            elif pivot > kthLargest:
                hi = pivot - 1
            else:
                lo = pivot + 1

    def heapSol(self, nums: List[int], k: int) -> int:
        heap = []
        for val in nums:
            heappush(heap, val)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def partition(self, nums: List[int], lo: int, hi: int, pivot: int) -> int:
        pivotIdx, pivotVal = lo, nums[pivot]
        # move true pivot value to end
        nums[pivot], nums[hi] = nums[hi], nums[pivot]   

        for i in range(lo, hi):
            # incrementally move smaller values to the left of the pivot index
            if nums[i] < pivotVal:
                nums[i], nums[pivotIdx] = nums[pivotIdx], nums[i]
                pivotIdx += 1

        # recall hi contains the pivot; so swap it with the real pivot idx
        nums[hi], nums[pivotIdx] = nums[pivotIdx], nums[hi]
        return pivotIdx 

'''
The goal is to find the kth largest element in the array, but without
sorting it first.

use minheap of size k
- values smaller than kth largest eventually get popped, while 
    values larger than kth largest stay in the min heap
- time: nlogk
    n items get passed into a min heap of size k
- space: k
    min heap of size k is maintained

use quickselect until the partition index is the same as the kth index
    - used to work until lc added a testcase with 50000 duplicates.
    - can use 3way quickselect, but idc at this point
'''
