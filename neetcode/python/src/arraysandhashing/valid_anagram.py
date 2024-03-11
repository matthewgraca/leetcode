class Solution:
    def isAnagram(s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        return sortedS == sortedT 

    def isAnagram2(s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()
        for i in s:
            if i in dictS:
                dictS[i] = dictS[i] + 1
            else:
                dictS[i] = 1
        for j in t:
            if j in dictT:
                dictT[j] = dictT[j] + 1
            else:
                dictT[j] = 1
        return dictS == dictT
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

That was the cheeky answer (also it's slower), so let me do it again with
hashmaps(dictionary). The idea here is that we create two dictionaries, one 
for each string, and compare the two dictionaries.

This is better than a naive approach because despite it being costly to 
create the dictionaries, the compare portion is really fast, so it makes 
up for the cost; O(n) for n letters, versus O(n^2) for n letters.

Pattern: when you see "compare", think dictionaries.

Time: 2 * n for the creation of the two dictionaries, n for the comparison 
between the two dictionaries.
    - O(n)
Space: 2 * n for the dictionaries
    - O(n)
'''
