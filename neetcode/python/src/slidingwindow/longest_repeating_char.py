class Solution:
    def characterReplacement(s: str, k: int) -> int:
        left = 0
        freq = dict()
        length = 0
        for right in range(len(s)):
            # frequency map of chars in the window
            freq[s[right]] = freq.get(s[right],0) + 1

            # number of characters needing replacement in the window = 
            # length of the window - the maximum character frequency
            windowLen = right - left + 1
            replacesNeeded = windowLen - max(freq.values())
            if replacesNeeded > k:
                freq[s[left]] -= 1
                left += 1
            else:
                length = max(length,windowLen)
        return length 
