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

The trace:
start loop
    - check a. is palindrome, add to partition
        - check a. is palindrome, add to partition
            - check b. is palindrome, add to partition
                - end of s reached, add partitions to res
                - b is popped
                - end of loop. backtrack
            - a is popped.
            - end of loop. backtrack
        - check ab. is not palindrome
            - end of loop. backtrack
        - end of loop. backtrack
    - check aa. is palindrome, add to partition
        -check b. is palindrome, add to partition
            -end of s reached; add partition to res
            - b is popped
            - end of loop. backtrack
        - end of loop. backtrack
    - check aab. is not palindrome. backtrack
    - end of loop
end loop
'''
