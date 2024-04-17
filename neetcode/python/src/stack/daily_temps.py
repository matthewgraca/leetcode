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

'''
initially thought this was a sliding window/two pointer problem. 
What about this problem means we can't use that method? I've triedand it doesn't work obviously, but how can I tell from the get-go 
this isn't two pointer so I don't waste time trying to force it?

the idea is that the stack saves values when the function (drawn by temps) is decreasing. When a 
temp larger than the top of the stack is encountered, that means there is a day of increasing temp.
So we pop from the stack, the days where the temp is decreasing -- we don't pop the day with a higher 
temp, because from that day to this current day the temp hasn't gotten high enough.

pattern? bruh idk, finding maxes and highest value in the array seems to be a monotonically inc/dec stack/deque problem??
It kind of keeps track of when a function (values in an array) is decreasing or increasing, and with clever pops you can 
get intresting things like local mins/maxes, (local min along with distance between points on this minimum).

time: n -- array is traversed, stack can potentially add n items
space: n -- stack can have potentially n items if temps is monotonically decreasing
'''
