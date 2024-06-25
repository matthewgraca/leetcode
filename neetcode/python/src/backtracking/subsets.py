from typing import List

class Solution:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            res.append([nums[i]])
            self.backtrack(i, nums, [], res)
        return res

    def backtrack(self, i: int, nums: List[int], sol: List[int], res: List[List[int]]) -> None:
        # base case: end of nums reached
        if i >= len(nums):
            res.append(sol)
            return
        
        # left branch: add from nums
        res.append(sol)
        self.backtrack(i+1, nums, sol + [nums[i]], res)

