from typing import List

class Solution:
    def __init__(self):
        pass

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, 0, row, col, set()):
                        return True
        return False
        
    def dfs(self, 
        board: List[List[str]], 
        word: str, 
        i: int, 
        row: int, 
        col: int,
        visited: set
    ) -> bool:
        # solution: word finished searching
        if i >= len(word):
            return True
        
        if not self.promising(board, row, col, i, word, visited):
            return False
        
        # otherwise, it's promising:
        # continue dfs on each direction
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited.add((row, col))
        for dr, dc in directions:
            r, c = dr + row, dc + col
            if self.dfs(board, word, i + 1, r, c, visited):
                return True
        visited.remove((row, col))

        # search ends with no solution
        return False

    # not promising:
    # 1. out of range
    # 2. cells already visited
    # 3. cell doesn't contain the necessary letter
    def promising(
        self,
        board: List[List[str]],
        row: int,
        col: int,
        i: int,
        word: str,
        visited: set
    ) -> bool:
        return (
            row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and
            (row, col) not in visited and
            word[i] == board[row][col]
        )
