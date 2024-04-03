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
