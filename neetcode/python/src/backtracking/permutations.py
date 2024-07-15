from typing import List

class Solution:
    def __init__(self):
        pass

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, set(), [], res)
        return res

    def backtrack(
        self,
        nums: List[int],
        visited: set,
        permutation: List[int],
        res: List[List[int]]
    ) -> None:
        # check solution
        if len(permutation) == len(nums):
            res.append(permutation.copy())
            return
        
        # check each position
        # e.g. build all solutions starting from 1, then all solutions from 2, etc..
        for num in nums:
            # promising function
            if num not in visited:
                # pre order
                visited.add(num)
                permutation.append(num)

                self.backtrack(nums, visited, permutation, res)

                # post order
                permutation.pop()
                visited.remove(num)
            # not promising if visited already, check next num
        # every num checked; backtrack
        return

'''
instead try to pick from nums by removing values from nums??

idk man
'''
