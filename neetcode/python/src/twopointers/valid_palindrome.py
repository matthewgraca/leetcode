class Solution:
    def isPalindrome(s: str) -> bool:
        # clean the string to only contain alphanumeric characters
        cleanS = str()
        for c in s:
            if c.isalnum():
                cleanS += c.lower()

        # check for palindrome
        left = 0
        right = len(cleanS) - 1
        while left < right:
            if cleanS[left] != cleanS[right]:
                return False
            left += 1
            right -= 1
        return True
