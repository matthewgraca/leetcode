from typing import List

class Solution:
    def __init__(self):
        pass

    def combinationSum2(
        self, 
        candidates: List[int], 
        target: int 
    ) -> List[List[int]]:
        res = []
        candidates.sort()
        self.checkNode(0, 0, target, candidates, [], res)
        return res

    def checkNode(
        self,
        i: int,
        comboSum: int,
        target: int,
        candidates: List[int],
        combo: List[int],
        res: List[List[int]]
    ) -> None:
        # solution
        if comboSum == target:
            res.append(combo.copy())
            return

        # not promising; backtrack
        if comboSum > target or i >= len(candidates):
            return

        # check solutions starting from candidates[0] to candidates[-1]
        prev = -1
        for j in range(i, len(candidates)):
            # recursive step
            # skip if we already checked solutions with c[j] as the starting point 
            if candidates[j] != prev:
                combo.append(candidates[j])
                self.checkNode(
                    j + 1, comboSum + candidates[j], 
                    target, candidates, combo, res
                )
                combo.pop()
                prev = candidates[j]
        return
'''
we start with, say, 1, we explore all the sums that start with 1 that can 
add up to the target. basically an exersise in calculating the sum of the subsets

we gather all those solutions, then move on to the next number. If the number 
is 1 again, we may end up making a lot of duplicate solutions; so we just skip over
it if we've started the solution with that number already
'''
