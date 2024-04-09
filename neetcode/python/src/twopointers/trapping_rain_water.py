from typing import List
class Solution:
    def trap(height: List[int]) -> int:
        waterOnColumn, area = 0, 0
        left, right = 0, len(height)-1
        maxLeftWall, maxRightWall = height[left], height[right]

        while left < right:
            # move the smallest column
            # if the next column is smaller, there will be water on top of it
            if maxLeftWall < maxRightWall:
                left += 1
                maxLeftWall = max(maxLeftWall,height[left]) 
                waterOnColumn = maxLeftWall - height[left]
            else:
                right -= 1
                maxRightWall = max(maxRightWall,height[right])
                waterOnColumn = maxRightWall - height[right]
            area += waterOnColumn
        return area 
