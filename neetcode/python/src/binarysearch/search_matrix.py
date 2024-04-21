from typing import List

class Solution:
    def __init__(self):
        pass

    '''
    same as binary search for a single dimension array, just dealing with annoying indexing
    alternatively, instead of silly indexing, we can just use the classic binary search
    while using a for loop for each row, since it's fundamentally an array of arrays
    '''
    def searchMatrix(self, matrix: List[int], target: int) -> bool:
        for m in range(len(matrix)):
            targetFound = self.recursive_search(matrix[m], target, 0, len(matrix[m])-1)
            if targetFound:
                return True
        return False

    def recursive_search(self, nums: List[int], target: int, start: int, end: int) -> bool:
        mid = (end + start) // 2
        # base case 1: targe not found
        if start > end:
            return False 
        # base case 2: target found
        if nums[mid] == target:
            return True 

        # left branch: target is in upper array
        if target > nums[mid]:
            return self.recursive_search(nums, target, mid+1, end)

        # right branch: target is in lower array
        if target < nums[mid]:
            return self.recursive_search(nums, target, start, mid-1)
'''
time : given mxn range, logn to search each m for a total of mlogn
space: no extra used; O(1)
'''
