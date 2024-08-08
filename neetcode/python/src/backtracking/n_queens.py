from typing import List

class Solution:
    def __init__(self):
        pass

    def solveNQueens(self, n: int) -> List[List[str]]:
        # nxn board initialized with '.'
        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        self.expand(0, board, set(), set(), set(), res)
        return res 

    def expand(
        self,
        row: int,
        board: List[List[str]],
        mainDiag: set,
        antiDiag: set,
        columns: set,
        res: List[List[str]]
    ) -> None:
        # solution: all queens have been placed
        if row == len(board):
            # 2d array -> 1d array by merging columns
            copy = [''.join(rows) for rows in board]
            res.append(copy)
            return

        # no solution and not attacked; place a queen here
        # place the next queen 
        for col in range(len(board)):
            # if a queen in this position is attacked, skip and check next column 
            if self.promising(row, col, antiDiag, mainDiag, columns):
                self.addQueen(board, row, col, antiDiag, mainDiag, columns)
                self.expand(row + 1, board, mainDiag, antiDiag, columns, res)
                self.removeQueen(board, row, col, antiDiag, mainDiag, columns)

        # no valid queen column placement; backtrack
        return

    def promising(self, row: int, col: int, antiDiag: set, mainDiag: set, columns: set) -> bool:
        return (
            row + col not in antiDiag and
            row - col not in mainDiag and
            col not in columns
        )

    def addQueen(
        self, 
        board: List[List[str]], 
        row: int, 
        col: int, 
        antiDiag: set, 
        mainDiag: set,
        columns: set
    ) -> None:
        board[row][col] = "Q"
        antiDiag.add(row + col)
        mainDiag.add(row - col)
        columns.add(col)

    def removeQueen(
        self, 
        board: List[List[str]], 
        row: int, 
        col: int, 
        antiDiag: set, 
        mainDiag: set,
        columns: set
    ) -> None:
        board[row][col] = "."
        antiDiag.remove(row + col)
        mainDiag.remove(row - col)
        columns.remove(col)
