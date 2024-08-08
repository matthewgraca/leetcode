from typing import List

class Solution:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, [], res)
        return res

    def backtrack(
        self, 
        i: int, 
        nums: List[int], 
        subset: List[int], 
        res: List[List[int]]
    ) -> None:
        # solution case: index passes length of nums
        if i >= len(nums):
            # build solution in post-order manner
            res.append(subset.copy())
            return

        # preorder dfs build solution
        subset.append(nums[i])
        self.backtrack(i + 1, nums, subset, res)

        # use another running index for next subset
        subset.pop() 
        self.backtrack(i + 1, nums, subset, res)

        return
