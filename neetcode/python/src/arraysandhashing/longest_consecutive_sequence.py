from typing import List
class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        while numSet:
            count = 1
            val = numSet.pop()
            
            # check left
            left = val - 1
            while left in numSet:
                numSet.remove(left)
                count += 1
                left -= 1

            # check right
            right = val + 1
            while right in numSet:
                numSet.remove(right)
                count += 1
                right += 1

            longest = max(longest,count)
        return longest
