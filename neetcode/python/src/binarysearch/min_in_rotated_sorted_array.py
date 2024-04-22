from typing import List

class Solution:
    def __init__(self):
        pass

    def findMin(self, nums: List[int]) -> int:
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
        return nums[mid]

'''
Seems like they mean rotation in a cyclical manner, e.g. one rotation is [1,2,3] -> [3,2,1]

the goal is to find the minimum value in this array. note that it is initially sorted, and is then rotated [1,n] times

preliminary ideas:
    since this is sorted, a linear search seems like the easiest; get a value, keep moving until you reach a larger value.

    but since this is (kind of) a sorted array, there should be a way we can do better and get a logn solution, which is better than linear.
    the number of times the array got rotated can maybe be used for indexing purposes for binary search?

    I think the most important thing to keep in mind is that we need to return the MINIMUM of the array. I think that'll allow us to effectively prune a lot of the problem, no?
        For example, if we have [1,2,3,4,5] and it was rotated 3 times [3,4,5,1,2]. it seems like there's an O(1) way to tell if an array has been rotated (check the first and last value; if the first value is larger, then rotation occured).
        I think it may just be a reformatting of the conditionals in the binary search.
            how should we cut the array in half? this is the most important question
            if the middle value is larger than the lower and upper values, do we cut out the left array?
                i think so. this means rotation occurred, and the values left of middle are decreasing. but more importantly, if the value at the upper index is smaller than the middle index, then the decreasing values must wrap around and be even smaller than the values in the left array

        Let's try this out programmatically:
            if middle > upper:
                # cut out lower array
                # \ * \
                lower = middle+1
            elif middle < upper:
                # cut out lower?
                # / * /
                upper = middle-1
            else:
                # found? not sure

        do we need to do anything about checking the lower index? does it matter?
            if middle < lower:
                # cut out lower array
                # \ * \
                lower = middle+1
            elif middle > lower:
                # cut out lower array?
                # / * /
                lower = middle+1

the lesson here is to to mark out your cases lol
time logn
space 1
'''
