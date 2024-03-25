'''
The idea here is to create a window containing the sequence of characters 
that generate a valid solution. You move the right pointer up if you can 
continute generating solutions (limited by k; the number of available character
replacements). Once k is reduced to 0, there are no more allowable character 
replacements, and the left pointer should be moved up.

We keep track of the characters inside the window with a hashmap. This hashmap 
helps us manage the different characters inside the window.

The trick here is "r-l+1 - max(count.values()) > k" This is saying that if the 
amount of characters that you need to replace in the window exceeds the amount 
of available replacements you have, then move the left pointer. We use 
max(count.values()) here because we don't want to replace the highest frequency 
characters, obviously; we want to only replace the smallest frequency ones.
'''
class Solution:
    def characterReplacement(s: str, k: int) -> int:
        l = 0
        res = 0
        windowCount = dict()
        for r in range(len(s)):
            # populate hashmap: {char, num of this char in the window}
            windowCount[s[r]] = 1 + windowCount.get(s[r], 0)

            # if the amount of chars you need to replace exceeds k, shift left ptr
            windowSize = r-l+1
            if windowSize - max(windowCount.values()) > k:
                windowCount[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
        return res
'''
Time: n to populate hashmap, n for compares, n to iterate through array
    - O(n)
Space: n to store the hashmap
    - O(n)
'''
