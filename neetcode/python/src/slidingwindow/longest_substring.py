class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        left, right = 0, 0
        substr = set()
        substrLength = 0
        while right < len(s):
            # if a duplicate is found, move left until it is removed
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            # add character to valid set, update length
            substr.add(s[right])
            right += 1
            substrLength = max(substrLength,right-left)
        return substrLength 
