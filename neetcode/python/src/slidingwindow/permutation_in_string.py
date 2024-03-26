'''
This is the one scenario where I think we are given the green light to 
actually check every permutation possible -- that is, in the case of s1 only.

To start off with, we want to collect every permutaion of s1 possible; then 
check those permutations against s2.

To check those against s2, we essentially do an element-wise comparision with 
s1's permutations and s2.

...

Well, we definitely can't store every permutation because it's n! space.

I recall an earlier problem where we found if one string was a valid anagram 
to another string; an anagram IS a permutation.

Now we have an O(n) way to check if one string is a permutation of another.
Now, we need to deal with situations where s2 is a different size from s1.

...

Seems very memory efficient! However, it is god awful slow, so let's find a 
way to make it faster.

Here I just make a second dictionary that contains the frequency of characters 
in the sliding window (whose size is the size of s1) to check for permutations.

'''
class Solution:
    def __init__(self):
        pass

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # case where there will be no valid permutations
        if len(s1) > len(s2):
            return False

        # dictionary containing letters and their frequencies in s1
        dictS1 = dict()
        for a in s1:
            dictS1[a] = 1 + dictS1.get(a,0)

        # initialize the sliding window dictionary
        l,r = 0, len(s1)-1
        dictS2 = dict()
        for i in range(r):
            dictS2[s2[i]] = 1 + dictS2.get(s2[i],0)

        while r < len(s2):
            # check for perm
            dictS2[s2[r]] = 1 + dictS2.get(s2[r],0)
            if dictS1 == dictS2:
                return True

            # else shift the window right
            if dictS2[s2[l]] == 1:
                del dictS2[s2[l]]
            else:
                dictS2[s2[l]] -= 1

            l += 1
            r += 1
        return False 

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)-1
        while r < len(s2):
            if self.isAnagram(s1,s2[l:r+1]):
                return True
            r += 1
            l += 1
        return False 

    def isAnagram(self,s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()
        for i in s:
            dictS[i] = 1 + dictS.get(i,0)
        for j in t:
            dictT[j] = 1 + dictT.get(j,0)
        return dictS == dictT

'''
Time: suppose m = len(s1), n = len(s2). 
 - m time to create s1's dictionary
 - n time to create s2's dictionary
 - s1's dictionary is compared to s2 n times, so that is m*n time
    - O(m*n)

Space: m for s1, and m for s2 since we delete keys outside of the window
    - O(m)
'''
