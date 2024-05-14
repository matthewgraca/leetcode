from typing import List
import math

class Solution:
    def __init__(self):
        pass

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (r + l) // 2

            # check how mid val fulfills H
            # H := hours to eat bananas at mid's rate
            H = 0
            for bananas in piles:
                H += math.ceil(bananas / mid)
            
            # use H val for binary search
            if H > h:
                l = mid+1
            else:
                r = mid-1
        
        # min k settles on the left value
        return l
