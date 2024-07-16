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
        return

    def isPalindrome(self, s: str, lo: int, hi: int):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True
'''
consider every subtring of s:
    -"aab" -> "aab", "aa", "ab", "a", "a", "b"
A partition of s makes up one group:
    -"aab" partitions into -> ["aab"], ["aa", "b"], ["a", "ab"], ["a", "b", "b"]
The goal is to find every group whose elements are palindromic:
    -which is: ["aa", "b"], ["a", "b", "b"]

1. calculate every partition of s
2. determine if every element in a given partition is palindromic
    -if yes, add to result

seems like raw dfs; i don't see how backtracking will work here?
A substring that is not palindromic can later become palindromic
A subtring that is palidromic can later become non-palindromic

There doesn't seem to be a way to fail-fast and backtrack

Though rechecking if a substring is palindromic seems expensive;
    -if palindromic and we add a letter, that makes it non-palindromic, no?
        -unless all the letters are the same

Actually, we just need to check if the incoming letter is the same as the beginning letter?
    -no need to make a palindrome function.
    - well b/c of partitioning it is better to just make a palindrome func
'''
