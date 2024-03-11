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
        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in dictNums:
                return [dictNums[j], i]
            dictNums[nums[i]] = i
        return [0,0]

'''
The first run, we did the naive method of comparing every combination of two 
numbers to find the target.

The second run was a bit tricky. At first I thought to check only combinations 
of the target; but it turns out that since the input can contain negative 
numbers, the number of possible combinations is actually infinite.

In order to limit the number of combinations I need to check, I got the 
target and subtracted it with the current number I have -- then compare 
that with a dictionary of all the numbers I've already checked. That way, 
I'm only looking for 1 number at a time, for n numbers. Normally this would 
be n^2, but with the magic of dictionaries, each search goes from n time to 
1 time; so over n searches, it's just n instead of n^2.

Time: n to create the dictionary, n to conduct n searches
    - O(n)
Space: n for the dictionary
    - O(n)

Pattern: I think the idea here is that when you are looking for combinations, 
you can boil it down to a searching problem. So if you can identify what 
exactly you are searching for, then you can make into a dictionary problem.
'''
