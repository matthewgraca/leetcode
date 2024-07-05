from typing import List
import heapq 

class Solution:
    def __init__(self):
        pass
    
    # 2n + k solution, min heap
    # space is n
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = x**2 + y**2 
            minheap.append((dist, x, y))

        heapq.heapify(minheap)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])

        return res

    # nlogk + k solution, max heap
    # space is k
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap; largest distances float up, then get popped when 
        # the heap grows beyond k; leaving closest (smallest) k distances
        maxheap = []
        for x,y in points:
            dist = x**2 + y**2 
            # preserve only the closest k points
            heapq.heappush(maxheap, (-dist, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        # get indices from heap, convert to points 
        res = []
        while maxheap:
            dist, x, y = heapq.heappop(maxheap)
            res.append([x,y])

        return res 
