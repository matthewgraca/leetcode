from typing import List

class Solution:
    def __init__(self):
        pass

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r + l) // 2
            left, mid, right = nums[l], nums[m], nums[r]

            # case 1: min value in left; trim right (mid may be min itself)
            if mid < right:
                r = m
            # case 2: min value in right; trim left (mid > right; can't be min)
            else:
                l = m+1
        
        return left
