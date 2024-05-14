from typing import List

class Solution:
    def __init__(self):
        pass

    def findMin(self, nums: List[int]) -> int:
        # binary search with special conditionals woooo
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r + l) // 2
            left, mid, right = nums[l], nums[m], nums[r]

            # case 1: continuous (strictly increasing)
            if left < right:
                r = m-1
            # case 2: discontinuous
            else:
                # case a: min value in left; trim right (mid may be min itself)
                if mid < right:
                    r = m
                # case b: min value in right; trim left
                else:
                    l = m+1
        
        return left
