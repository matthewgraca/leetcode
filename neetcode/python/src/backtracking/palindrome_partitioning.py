from typing import List

class Solution:
    def __init__(self):
        pass

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(
        self,
        s: str,
        i: int,
        partition: List[str],
        res: List[List[str]]
    ) -> None:
        # solution: s fully scanned, palindromes in partition
        if i >= len(s):
            res.append(partition.copy())
            return

        # start at each character
        for j in range(i, len(s)):
            # check if substring is a palindrome
            if self.isPalindrome(s, i, j):
                partition.append(s[i : j + 1])
                self.dfs(s, j + 1, partition, res)
                partition.pop()
            # if not, check substring adding next character
        # if no character can make a palindrome, backtrack
        return

    def isPalindrome(self, s: str, lo: int, hi: int):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True
