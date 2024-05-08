from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = ""
        res = []
        self.dfs(n, 0, 0, st, res)
        return res
        
    def dfs(self, n: int, opens: int, closes: int, st: str, res: List[str]) -> None:
        # base case: all parens added and matched
        if len(st) == 2*n:
            res.append(st)
            return

        # left branch: add open parens
        if opens < n:
            self.dfs(n, opens+1, closes, st + "(", res)
        
        # right branch: add matching closed parens
        if opens > closes:
            self.dfs(n, opens, closes+1, st + ")", res)

        # can't make well-formed parentheses; backtrack
        return
