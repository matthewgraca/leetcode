from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = [0]*n

        # scan forward. first pass generates prefix-only answers
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # scan backward. second pass finds product of prefix answers with suffix
        for i in range(n-1, -1, -1):
            ans[i] *= suffix 
            suffix *= nums[i]
            
        return ans
