from typing import List

class Solution:
    def __init__(self):
        pass

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
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
        # non promising
        if i >= len(candidates) or currSum > target:
            return
                    
        # solution
        if currSum == target:
            res.append(combo.copy())
            return

        # currSum < target = promising path
        currSum += candidates[i]
        combo.append(candidates[i])
        # try current element
        self.dfs(candidates, target, i, currSum, combo, res)
        
        # current element backtracked; try next element
        val = combo.pop()
        currSum -= val
        self.dfs(candidates, target, i + 1, currSum, combo, res)

        return
