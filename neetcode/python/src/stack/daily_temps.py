from typing import List

class Solution:
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for tempIdx in range(len(temperatures)):
            # stack contains decreasing temps
            while stack and temperatures[tempIdx] > temperatures[stack[-1]]:
                dayIdx = stack.pop()
                ans[dayIdx] = tempIdx - dayIdx 
            stack.append(tempIdx)
        return ans 
