from typing import List

class Solution:
    def __init__(self):
        pass

    def search(self, nums: List[int], target: int) -> int:
        # return self.recursive_search(nums, target, 0, len(nums)-1)

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (end + start) // 2
            # check upper half
            if target > nums[mid]:
                start = mid + 1
            # check lower half
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid 
        return -1

    def recursive_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        mid = (end + start) // 2
        # base case 1: targe not found
        if start > end:
            return -1
        # base case 2: target found
        if nums[mid] == target:
            return mid

        # left branch: target is in upper array
        if target > nums[mid]:
            return self.recursive_search(nums, target, mid+1, end)

        # right branch: target is in lower array
        if target < nums[mid]:
            return self.recursive_search(nums, target, start, mid-1)
'''
implemented both iterative and recursive solutions, god i suck at recursion

time: each iteration, the problem space is cut in half -- logn
space: no extra space is used. O(1)
'''
