class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        substr = set()
        substrLength = 0
        for right in range(len(s)):
            # if a duplicate is found, move left until it is removed
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            # add character to valid set, update length
            substr.add(s[right])
            substrLength = max(substrLength,right-left+1)
        return substrLength 
