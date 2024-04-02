from typing import List

class Solution:
    def twoSumNaive(nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [0,0]

    def twoSum(nums: List[int], target: int) -> List[int]:
        dictNums = dict()
        for i in range(len(nums)):
            search = target - nums[i]
            if search in dictNums:
                return [dictNums[search], i]
            dictNums[nums[i]] = i
        return [-1,-1]
