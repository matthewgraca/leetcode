from typing import List
import math

class Solution:
    def __init__(self):
        pass

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the upper and lower bound for eating rate
        lower, upper = 1, max(piles) 
        k = 0
        while lower <= upper:
            # hours needed to eat all piles
            hours = 0
            mid = (upper + lower) // 2
            for a in piles:
                hours += math.ceil(a / mid) 

            # binary search for min k
            if hours > h:
                lower = mid+1
            else:
            # even if value is found, keep searching for a smaller one
                k = mid
                upper = mid-1
        return k 
'''
I got the trick, but got stuck in implementation hell.
accidentally used the smallest value as the floor, when I should've used just 1

time:
    basically traverse numbers from 1 to max(piles), but apply binary search so
    those operands are contained in a log function
    O(n) to find the max value in piles
    O(n) traversal for every search, so multiply the n on the log func
    
    let n be the size of piles.
    we have O(nlog(max(piles)))

space: no extra space is used, O(1)

'''
