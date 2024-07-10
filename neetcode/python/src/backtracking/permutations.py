from typing import List

class Solution:
    def __init__(self):
        pass

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, [], res)
        return res

    def backtrack(
        self,
        i: int,
        nums: List[int],
        permutation: List[int],
        res: List[List[int]]
    ) -> None:
        # base case
        # copy valid permutation
        if len(permutation) == len(nums):
            res.append(permutation.copy())
            return
        # backtrack when no nums left to take from 
        if i >= len(nums):
            return
        
        # dfs recursive step
        permutation.append(nums[i])
        self.backtrack(i + 1, nums, permutation, res)
        permutation.pop()   # backtrack
        self.backtrack(i + 1, nums, permutation, res)
        return

'''
instead try to pick from nums by removing values from nums??
'''
