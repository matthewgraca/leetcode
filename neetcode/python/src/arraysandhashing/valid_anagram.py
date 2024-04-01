class Solution:
    def isAnagram(s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()
        for a in s:
            dictS[a] = 1 + dictS.get(a,0)
        for b in t:
            dictT[b] = 1 + dictT.get(b,0)
        return dictS == dictT

    def isAnagram2(s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)
        return sortedS == sortedT 
