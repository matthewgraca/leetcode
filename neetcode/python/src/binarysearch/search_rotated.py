from typing import List

class Solution:
    def __init__(self):
        pass

    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)-1
        
        # case 1: continuously increasing
        if nums[lower] < nums[upper]:
            # normal binary search
            while lower <= upper:
                mid = (upper + lower) // 2
                if target < nums[mid]:
                    upper = mid-1
                elif target > nums[mid]:
                    lower = mid+1
                else:
                    return mid
            return -1
        # case 2: discontinuous
        else:
            while lower <= upper:
                mid = (upper + lower) // 2
                # case a: mid is lower bound
                if nums[mid] < nums[upper]:
                    # case i: target found
                    if target == nums[mid]:
                        return mid
                    elif target == nums[upper]:
                        return upper
                    # case ii: target is in upper arr
                    if target < nums[upper] and target > nums[mid]:
                        lower = mid+1
                    # case iii: target is in lower arr
                    else:
                        upper = mid-1
                # case b: mid is upper bound
                else:
                    # case i: target found
                    if target == nums[mid]:
                        return mid
                    elif target == nums[lower]:
                        return lower
                    # case ii: target is in lower arr
                    if target < nums[mid] and target > nums[lower]:
                        upper = mid-1
                    # case iii: target is in upper arr
                    else:
                        lower = mid+1
            return -1

'''
        # finds the min value of a rotated sorted array, at index mid
        lower, upper = 0, len(nums)-1
        while lower <= upper:
            mid = (upper + lower) // 2
            l, m, u = nums[lower], nums[mid], nums[upper]
            # case 1: continuous increasing
            if l < u:
                upper = mid-1
            # case 2: discontinuity
            else:
                # case a: mid is lower bound
                if m < u: 
                    upper = mid
                # case b: mid is upper bound
                else:
                    lower = mid+1

'''
