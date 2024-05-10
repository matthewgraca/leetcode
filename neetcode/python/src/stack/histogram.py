from typing import List

class Solution:
    def largestRectangleArea(heights: List[int]) -> int:
        # stack will contain [start index, height]
        # where the height is the height and the index this height goes back to
        # e.g. (0,6) means the height of 6 goes back to the 0th index
        stack = []
        maxArea = 0
        # heights.append(0) # see comments at end of functions

        for i, h in enumerate(heights):
            start = i
            # if the height in the array is decreasing, retroactively calculate
            # the areas utilizing all the larger rectangles
            while stack and h <= stack[-1][1]:
                start, height = stack.pop()
                # area = smallest height of sequence * (end index - start index)
                maxArea = max(maxArea, height * (i - start))
            stack.append((start, h))

        # necessary for monotonically increasing heights
        # it is also possible to append 0 to heights as a sentinel value,
        # guaranteeing a decreasing value at the end. But that just obfuscates
        # the code, with no meaningful performance or readability boost
        while stack:
            start, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - start))

        return maxArea
