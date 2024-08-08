from typing import List

class Solution:
    def __init__(self):
        pass

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, 0, [], res)
        return res
        
    def dfs(self, 
        candidates: List[int], 
        target: int, 
        i: int, 
        currSum: int, 
        combo: List[int], 
        res: List[List[int]]
    ) -> None:
        # solution
        if currSum == target:
            res.append(combo.copy())
            return
        
        # non promising
        if i >= len(candidates) or currSum > target:
            return
                    
        combo.append(candidates[i])
        currSum += candidates[i]
        self.dfs(candidates, target, i + 1, currSum, combo, res)
        currSum -= combo.pop()

        # avoid using duplicate values already considered
        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1
        self.dfs(candidates, target, i + 1, currSum, combo, res)
        return
