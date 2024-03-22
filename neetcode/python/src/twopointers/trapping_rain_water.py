from typing import List

'''
This is so hard... this isn't a two pointers problem, it's a four pointers 
problem man...

So to try to explain this solution, we have a left and right pointer that 
is strictly used for us to calculate how much water is on top of that 
right or left index. The max left and max right pointers tell us the 
length of the walls that left or right is contained in, which tells us 
how much water should be on top of either left or right.

We move either the left or right pointer, depending on which wall 
is taller. We only care about the shorter wall because the area of water 
in a well is limited by the shortest wall; the larger wall can be 
10,000,000 units taller and it would not matter.

This is the key idea: there could be another wall of infinite size, 
with a set of infinite amount of wells between the well you're at 
and the other wall; it does not matter. At your current well, you 
are limited by the shortest wall, no matter how far and how tall 
that other wall is; that's why we can have the other pointer in 
some far off land that we don't care about.

Once we get the water that is on top of whatever left/right index, 
we move on to the next index, making sure that if there are any 
changes to the smallest wall, we keep note of it.
'''
class Solution:
    def trap(height: List[int]) -> int:
        area = 0
        left, right = 0, len(height)-1
        maxLeftWall, maxRightWall = height[left], height[right]

        while left < right:
            if maxLeftWall < maxRightWall:
                left += 1
                maxLeftWall = max(maxLeftWall,height[left]) 
                area += maxLeftWall - height[left]
            else:
                right -= 1
                maxRightWall = max(maxRightWall,height[right])
                area += maxRightWall - height[right]
        return area 
'''
Time: n to scan the array
    - O(n)
Space: no extra space
    - O(1)
'''
