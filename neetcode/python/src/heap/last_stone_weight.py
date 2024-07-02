from typing import List
import heapq

class Solution:
    def __init__(self):
        pass

    def lastStoneWeight(self, stones: List[int]) -> int:
        # certified python moment: make max heap from stones
        stoneMaxHeap = [-stone for stone in stones]
        heapq.heapify(stoneMaxHeap)

        # continue as long as there are 2 stones
        while len(stoneMaxHeap) > 1:
            x, y = heapq.heappop(stoneMaxHeap), heapq.heappop(stoneMaxHeap)
            # x >= y
            # if diff size, smash together and add back to heap
            if x != y:
                heapq.heappush(stoneMaxHeap, x - y)
        
        # return 0 if the heap is empty, otherwise return the top val, inverted
        return 0 if not stoneMaxHeap else -stoneMaxHeap[0]
