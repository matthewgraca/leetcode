class Solution:
    def isAnagram(s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        return sortedS == sortedT 

'''
The way I interpret the word "anagram" is it essentially asks if one word is a 
shuffled version of another word. So to check if one word is a shuffled 
version of another word, we can just sort both words and check if they end up 
being the same word after.

To simplify, suppose n is the size of the largest string of the two
Time: 2 * nlogn for the sorts, n for the compare
    - O(nlogn)
Space: 2n to store the sorted strings
    - O(n) 
'''
