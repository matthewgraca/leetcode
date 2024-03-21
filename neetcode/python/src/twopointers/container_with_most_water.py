from typing import List

'''
naive n^2 solution:
        maxArea = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                currArea = min(height[i], height[j]) * (j-i)
                maxArea = max(maxArea, currArea)

Instead of moving the smallest bar between h[l+1] and h[r-1], we should 
instead move the smallest bar between h[l], h[r]

As a quick explanation after solving, the trick here is that we don't 
really need to test every single combination, because the bars that 
are "encased" in the water of another container 100% have less area than 
the container it is inside of. 
    -i.e.: we do not care about smaller bars inside our current container

The only thing that may throw a wrench into this line of thinking are bars 
that are larger or "stick out" from inside the current container -- it turns 
out that those are the only ones we really need to check.
    -i.e.: we care about larger bars in our current container, b/c it might 
    generate a larger area (esp. if you are changing the SMALLER of the two 
    bars, since the smaller bar limits the size of the container)
'''
class Solution:
    def maxArea(height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0
        while (left < right):
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currArea)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
        return maxArea

'''
I kinda brute forced this a little bit; just running it with a different 
idea until it worked. However, I don't think this method works if I don't 
have a test suite with me.

Time: n to scan the array
    - O(n)
Space: no extra space
    - O(1)
'''
