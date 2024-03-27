'''
Classic sliding window with the additional frequenct map for characters in 
a string. I got the trick down relatively fast, but the implementation 
details screwed me over quite a bit; managing have/need values I think was 
what did me in, because it messed with my left pointer movement.
'''
class Solution:
    def minWindow(s: str, t: str) -> str:
        window = dict()
        targets = dict()
        for key in t:
            targets[key] = 1 + targets.get(key,0)

        minSize, size = float('inf'), 0
        minL, minR = 0,0
        have,need = 0,len(t)
        l,r = 0,0
        for r in range(len(s)):
            # add char to window; if it matches a target and its count, add to have
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in targets and window[s[r]] <= targets[s[r]]:
                have += 1

            # checks if min substring is found
            while have == need:
                # check if substring is smaller than our current min substring
                size = r-l+1
                if size < minSize:
                    minSize = size
                    minL,minR = l,r
                # move left window
                window[s[l]] -= 1
                # if removal took away a necessary chararcter, decrement have
                if s[l] in targets and window[s[l]] < targets[s[l]]:
                    have -= 1
                l += 1
        # return empty string if no minimun substring found
        return s[minL:minR+1] if minSize != float('inf') else "" 
'''
Suppose the string s and t are of size m and n, respectively.
Time: n to create the map of t, m to traverse s, m to create the map of s
    - O(m + n)
Space: n for the map of t, m for the map of s
    - O(m + n)
'''
