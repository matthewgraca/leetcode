from typing import List

class Solution:
    def __init__(self):
        pass

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, [], res)
        return res

    def backtrack(
        self, 
        i: int, 
        nums: List[int], 
        subset: List[int], 
        res: List[List[int]]
    ) -> None:
        # base case: valid subset
        if i >= len(nums):
            res.append(subset.copy())
            return

        # preorder dfs build solution
        subset.append(nums[i])

        # left step condition:
        self.backtrack(i + 1, nums, subset, res)
        subset.pop() # left tree end; pop and go to right tree
        # right step condition:
        self.backtrack(i + 1, nums, subset, res)
        return
'''
Ideas around backtracking:
- basically, it is a dfs traversal over a problem that requires generating combinations
    - so think of a the problem as a tree where each node is a combination
    - you just dfs through; (post order or pre order?)
        - i think it's preorder since we pass changed data through as a function argument, so 
            that means changes were made before the function call
- some key ideas:
    - base case: this is when you've reached a valid solution
    - conditionals for left/right movement
        - you encase the left/right recursive step in a conditional -- 
            - if the condition is not met, that means no more solutions can be made down that 
                path, so go right. if that path eventually closes, you'll hit the end of the func. 

curr problem
- pre order dfs traversal. subset is built in preorder dfs manner, res is built in postorder manner.
- subset is itself a stack. since we pass the reference it doesn't respond to recursion, so we have 
    to pop it so it follows the recursive calls.

Time:
O(2^n) - this many combinations generated

space:
O(2^n) - this many calls on the function stack
'''
