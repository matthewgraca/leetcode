from typing import List

class Solution:
    def __init__(self):
        pass

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # put duplicates together for easy skipping
        self.checkNode(0, nums, [], res)
        return res

    def checkNode(
        self,
        i: int,
        nums: List[int],
        subset: List[int],
        res: List[List[int]]
    ) -> None:
        # solution 
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # recursive step
        # left tree: running index
        subset.append(nums[i])
        self.checkNode(i + 1, nums, subset, res)
        subset.pop()

        # instead of using the next index over,
        # scan over the duplicates so a unique value is used in our right tree 
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.checkNode(i + 1, nums, subset, res)
        return
