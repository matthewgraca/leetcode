from typing import List
class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right] 
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left+1, right+1]
        return [0,0]
