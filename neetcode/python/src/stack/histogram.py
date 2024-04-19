from typing import List

class Solution:
    def largestRectangleArea(heights: List[int]) -> int:
        # contains (border, height) 
        # e.g. (0,6) means height 6 goes back to idx 0
        stack = []
        maxArea = 0
        minHeight = float('inf')
        for i,height in enumerate(heights):
            if not stack:
                stack.append((i,height))
            elif height <= stack[-1][1]:
                # pop and compute areas until smaller border is reached
                left = 0
                while stack and height <= stack[-1][1]:
                    left, prevHeight = stack.pop()
                    maxArea = max(maxArea, prevHeight * (i - left))
                stack.append((left,height))
            else:
                stack.append((i,height)) 

        # compute remaining areas
        n = len(heights)
        while stack:
            left, height = stack.pop()
            maxArea = max(maxArea, height * (n - left))

        return maxArea
'''
the idea here is saving higher and higher heights (monotonic stack).
When we see a height that is smaller, we go back to compute the max areas 
from those heights

The trick here is the data in the stack. we need to push in the height 
and the index; but the index is not where the height bar is -- rather, it 
is a value that tell us "how far back this height goes". This is necessary 
because when the function is decreasing, the previous heights also decline 
to match the current smaller height <-- this is reminiscent of the fleet problem.

The biggest issue here is I thought this was a sl window / two pointer problem...
it's honestly hard to differentiate stack problems like this and those 
problems, especially sliding window. because we really are evaluating a 
window(subset) of values, just with the added idea of "saving mins" or maxes.

time - n to append and pop from stack and to traverse the input array
space - n space for the stack
'''
