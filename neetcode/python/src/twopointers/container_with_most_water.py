from typing import List
class Solution:
    def maxArea(height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height)-1
        while (left < right):
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currArea)

            # move the smallest wall; if they're the same, arbitrarily move the left
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxArea
