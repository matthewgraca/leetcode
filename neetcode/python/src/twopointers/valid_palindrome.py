'''
palindrome:
    1. convert all uppercase letters into lowercase letters
    2. remove all non-alphanumeric characters
    3. reads the same forward and backward (so only letters and numbers)

checking for palindrome:
two pointers, one at each end of the string, check if they're the same character.
End once the two pointers converge at the middle of the string.
'''
class Solution:
    def isPalindrome(s: str) -> bool:
        # clean the string to only contain alphanumeric characters
        cleanedS = str()
        for c in s:
            if c.isalnum():
                cleanedS += c.lower()

        # check for palindrome
        i = 0
        j = len(cleanedS) - 1
        while i < j:
            if cleanedS[i] != cleanedS[j]:
                return False
            i += 1
            j -= 1
        return True

'''
wow I banged out this solution in 15 mins I feel so cool.

Nothing much to say here, but knowing the trick is that with palindromes, 
you are checking one side of an array with the other side; making it a 
clear choice to use two pointers to check one side while the other pointer 
checks the other.

Time: n to clean the string, n/2 to check the palindrome
    - O(n)
Space: n to create a cleaned string
    - O(n)
'''
