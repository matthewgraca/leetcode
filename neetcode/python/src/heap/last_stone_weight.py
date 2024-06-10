from typing import List
from heapq import *

class Solution:
    def __init__(self):
        pass

    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap of stones
        stoneHeap = [-val for val in stones]
        heapify(stoneHeap)

        # smash stones until only 1 or 0 remain
        while len(stoneHeap) > 1:
            # by max heap invariant, x >= y
            # x > y : new stone added; else x = y : both consumed
            x, y = -heappop(stoneHeap), -heappop(stoneHeap)
            if x > y:
                heappush(stoneHeap, -1 * (x - y))

        return -stoneHeap[0] if stoneHeap else 0
'''
yeah this is clearly a heap problem.
    pop top 2, push result
    continue until one value remains; if none remain, return 0

the only question is that we're asked to pop the largest two -- so 
I think it's time to do our max heap tricks

list comprehension seems faster; but what's a lot better is utilizing the 
fact that heapify is n time, so it's better to use that over creating the heap in
nlgn time

time:
    - heap of n items is created
        - n time to invert the input
        - n time to heapify it
    - for each pass we pop 2 and add 1; essentially decrementing by 1 each pass, taking n time
    - over all, it's n time

space:
    - need n space for the heap
'''
