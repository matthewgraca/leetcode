from typing import List

class Solution:
    def __init__(self):
        pass

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(0, 0, target, candidates, [], res)
        return res

    def backtrack(
        self,
        i: int,
        comboSum: int,
        target: int,
        candidates: List[int],
        combo: List[int],
        res: List[List[int]]
    ) -> None:
        # base case 1: sum greater than target or run out of candidates
        # no solution past here; back track
        if comboSum > target or i >= len(candidates):
            return
        # base case 2: sum equal to target
        # solution found: add to result and backtrack
        if comboSum == target:
            res.append(combo.copy())
            return

        # preorder dfs construct the combination
        combo.append(candidates[i])
        self.backtrack(i, comboSum + candidates[i], target, candidates, combo, res)
        combo.pop() # backtrack
        self.backtrack(i + 1, comboSum, target, candidates, combo, res)
        return
'''
backtracking is an exercise in generating and traversing a decision tree. the decision 
here is adding duplicates vs distinct candidates
- that is, left tree adds the current item (dupe), right tree adds the next item (distinct).
- backtrack on two conditions: 
    - can't generate solution (sum > target) or out of candidates (i >= len(candidates)
    - solution found (sum == target)
so normally we backtrack when we reach the leaf node, but in this case we know high up in the 
tree that this won't branch into a solution, so we fail fast and backtrack. This solution 
also includes the classic version where if we find a solution, then we add it to the result 
and trigger the backtrack

This problem has some slight quirks. we update the combo sum when going in the left tree, 
but not when we go to the right.

I GET IT NOW, IVE BEEN WRITING THE TREES WRONG THE ENTIRE TIME. When you pop you aren't 
"returning" back, you are making a NEW DECISION.
- "left" is just using the same item, updating the sum
- "right" is using the next item

It's still kind of confusing, because it's not really 100% dfs since we have this extra 
stack; the sum is updated only once.

i think the way to go about it is think of backtracking as traversing a decision tree.
When you contruct this decision tree, think about each recursive call being a decision
- in this case, left is decision to stay, right is decision to move

if the stay eventually returns, that means we need to backtrack and make a decision to do the 
    other thing; that includes popping then calling the right path.
'''
