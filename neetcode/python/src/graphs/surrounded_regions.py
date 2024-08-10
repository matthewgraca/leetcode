from typing import List

class Solution:
    def __init__(self):
        pass

    def solve(self, board: List[List[str]]) -> None:
        # run dfs on the border Os, and flip them to Zs
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if self.isBorderIdx(board, row, col) and board[row][col] == 'O':
                    self.dfs(board, row, col, visit)

        # All cells w/ Zs are uncapturable Os
        # All cells w/ Os are capturable
        # second pass: flip all Os to Xs, then all Zs to Os
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'Z':
                    board[row][col] = 'O'
        
        return

    # marks all Os adjacent to the source as Z
    def dfs(self, board: List[List[str]], row: int, col: int, visit: set) -> None:
        visit.add((row, col))
        board[row][col] = 'Z'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.promising(board, r, c, visit):
                self.dfs(board, r, c, visit)
        
        return
    
    def promising(self, board: List[List[str]], row: int, col: int, visit: set) -> bool:
        ROWS, COLS = len(board), len(board[0])
        return (
            # indices in range
            row >= 0 and col >= 0 and
            row < ROWS and col < COLS and
            # cell not already visited
            (row, col) not in visit and
            # is a cell containing 'O'
            board[row][col] == 'O'
        )
    
    def isBorderIdx(self, board: List[List[str]], row: int, col: int) -> bool:
        ROWS, COLS = len(board), len(board[0])
        return row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1
