from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        # create a monotonically decreasing deque, containing indicies of nums
        # this has two characteristics:
        # 1. the leftmost contains the max value of the window; other others
        #   contain possible maxes of that window
        # 2. these contain indices instead of values, so the deque can update 
        #   based on the left pointer's location
        maxes = deque()

        res = []
        left = 0
        for right in range(len(nums)):
            # remove smaller values than nums[right]; as long as nums[right]
            # is in the window, these values won't be a potential max.
            while maxes and nums[maxes[-1]] < nums[right]:
                maxes.pop()
            maxes.append(right)

            # maxes should only contain window values. pop if left pointer passes
            if left > maxes[0]:
                maxes.popleft()

            # start adding to the result once the window reaches size. update left ptr
            if (right+1) >= k:
                res.append(nums[maxes[0]])
                left += 1

        return res 
