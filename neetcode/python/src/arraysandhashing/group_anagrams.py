from typing import List

class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        dictStrs = dict()
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in dictStrs:
                dictStrs[sortedS].append(s)
            else:
                dictStrs[sortedS] = [s]
        ans = list(list())
        for s in dictStrs:
            ans.append(dictStrs[s])
        return ans

'''
This solution makes use of the fact that every anagram of a word is the same 
string as the original if they are both sorted. With that in mind, we can 
take every string in the list, sort it, then compare it to a dictionary of 
strings. If it already exists, that string is put in the same group.

Again, the basic idea is were going to do a lot of searching; in this case, 
we sort the word and search our dictionary for the same string.

Also, Python is annoyinggggg.

Assuming n strings and each string has m characters
Time: n*mlogm for sorting every string in the list, 1 for comparing that sorted 
string with every key in the dictionary, n for constructing the solution.
    - O(n*mlogm)
Space: n for the dictionary, n for the solution
    - O(n)
'''
