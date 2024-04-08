from typing import List
class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        target = 0
        solution = []

        # two sum with sorted array, including a third pointer: nums[i]
        for i in range(len(sortedNums)-2):
            # avoid evaluating duplicate nums[i]
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            # classic two sum with sorted array
            left = i+1
            right = len(sortedNums)-1
            while left < right:
                currentSum = sortedNums[i] + sortedNums[left] + sortedNums[right]

                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    solution.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    # avoid evaluating duplicate nums[left]
                    while (left < right and sortedNums[left] == sortedNums[left-1]):
                        left += 1
        return solution
