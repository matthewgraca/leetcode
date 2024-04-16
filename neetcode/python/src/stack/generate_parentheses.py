from typing import List

class Solution:
    def __init__(self):
        pass

    def generateParenthesis(self, n: int) -> List[str]:
        res = []    # contains full solutions
        stack = []  # string containing parens
        self.backtrack(0, 0, n, stack, res)
        return res

    def backtrack(self, openCount, closedCount, n, stack, res):
        # leaf - base case: combination found
        if openCount == n and closedCount == n:
            res.append("".join(stack))
        
        # branch 1: open paren is addable
        if openCount < n:
            stack.append("(")
            self.backtrack(openCount+1, closedCount, n, stack, res)
            stack.pop()
        # branch 2: closed paren is addable 
        if closedCount < openCount:
            stack.append(")")
            self.backtrack(openCount, closedCount+1, n, stack, res)
            stack.pop()


'''
silly ass trick, the "stack" idea is using the function 
call stack for a backtracking algorithm along with this actual parenthesis stack

time : O(2^(2*n)) = O(4^n), but prunes a ton of solutions since we don't traverse the entire space
space: stack and result are linear; O(n)
'''
