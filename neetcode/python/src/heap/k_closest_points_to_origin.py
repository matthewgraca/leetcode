from typing import List
from heapq import *

class Solution:
    def __init__(self):
        pass
    
    # 2n + k solution, min heap
    # space is n
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            dist = self.square_distance_from_origin(points[i])
            heap.append((dist, i))

        heapify(heap)

        res = []
        for _ in range(k):
            dist, i = heappop(heap)
            res.append(points[i])

        return res

    # nlogk + k solution, max heap
    # space is k
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap; largest distances float up, then get popped when 
        # the heap grows beyond k; leaving closest (smallest) k distances
        heap = []
        for i in range(len(points)):
            dist = self.square_distance_from_origin(points[i])
            # preserve only the closest k points
            heappush(heap, (-dist, i))
            if len(heap) > k:
                heappop(heap)

        # get indices from heap, convert to points 
        res = []
        while heap:
            dist, i = heappop(heap)
            res.append(points[i])

        return res 

    # (x_a)^2 + (y_a)^2
    def square_distance_from_origin(self, a: List[int]) -> int:
        return a[0] * a[0] + a[1] * a[1]
'''
note: for all x,y > 0, if x > y, then sqrt(x) > sqrt(y) so if we use 
euclidian distance we don't have to actually calculate sqrt if we're just 
doing a distance comparison

for every value in points:
    1. calculate the square distance b/t the point and the origin
    2. push the distance and the index of the point into a min heap
        - if it's smaller, don't add
    3. pop the top k points, return as a list

max heap solution:
    time: nlogk + k = nlogk
    space: k
min heap solution:
    time: 2n + k = 2n
    space: n
'''
