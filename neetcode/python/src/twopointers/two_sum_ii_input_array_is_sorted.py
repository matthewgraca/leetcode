from typing import List

'''
-numbers is already sorted
-array is 1-indexed (start counting from 1 instead of classic 0)

The way I would like to approach this is to utilize the sorted nature 
of the array of numbers. So if we construct our sum using values from 
the start and end of the array, we can close in on a solution almost 
in a binary search manner.

So for example, in 2,7,11,15 with a target of 9: we take 2+15, find that 
the sum is larger than the target (so the sum needs to be smaller). Since 
the array is sorted, we can move the right operand left to get that smaller 
sum -> 2+11 = 13, etc. until we get 2+7 = 9. 

But suppose the target is 18. We start with 2+15 = 17, which means our sum 
needs to be larger. We increment the index of the left operand to raise the 
sum, getting us 7+15=22. The sum is now larger than the target, so we 
decrement the index of the right operand, giving us 7+11=18, our target.
'''
class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sumVal = numbers[left] + numbers[right] 
            if sumVal > target:
                right -= 1
            elif sumVal < target:
                left += 1
            else:
                return [left+1, right+1]
        return [0,0]
'''
Nothing to say, the top comment explains it. I suppose that the pattern 
of the array being sorted means that something like two pointers are more 
likely to be a solution, I suppose.

Time: n to scan the array
    - O(n)
Space: same space regardless of size
    - O(1)
'''
