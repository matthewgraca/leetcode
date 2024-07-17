from typing import List

class Solution:
    def __init__(self):
        pass

    def solveNQueens(self, n: int) -> List[List[str]]:
        # nxn board initialized with '.'
        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        self.checkNode(0, board, set(), set(), set(), res)
        return res 

    def checkNode(
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
            if not self.collision(row, col, antiDiag, mainDiag, columns):
                self.addQueen(board, row, col, antiDiag, mainDiag, columns)
                self.checkNode(row + 1, board, mainDiag, antiDiag, columns, res)
                self.removeQueen(board, row, col, antiDiag, mainDiag, columns)

        # no valid queen column placement; backtrack
        return

    def collision(self, row: int, col: int, antiDiag: set, mainDiag: set, columns: set) -> bool:
        return (row + col) in antiDiag or (row - col) in mainDiag or col in columns

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
'''
thrw this away b/c it don work and there's an interesting quirk of diagonals we can abuse
that is, the "main diagonal" of a matrix (top left to bottom right) are the same values
when subtracted from each other
    -e.g. 0-0 = 1-1 = 2-2 = 3-3

meanwhile, the antidiagonal (bottom left to top right) has the same values when added:
    -e.g. 3+1 = 2+2 = 1+3

This means we can use three sets to track invalid squares:
    -mainDiag, antiDiag, columns

So given a coordinate (row, col):
    - if row-col is in mainDiag, it is attacked
    - if row+col is in antiDiag, it is attacked
    - if col is in columns, it is attacked.

so yeah


    # determines if a given coordinate will attack a queen
    # we only check queens above the current coordinate
    def collision(self, board: List[List[str]], x: int, y: int) -> bool:
        # check columns above from [x-1 -> 0]
        for a in range(x-1, -1, -1):
            if board[a][y] == "Q":
                return True 

        # row not checked; we won't place queens on the same row
        
        # check upper right diag
        c, d = x - 1, y + 1
        while c >= 0 and d < len(board):
            if board[c][d] == "Q":
                return True 
            c, d = c - 1, d + 1

        # check upper left diag
        e, f = x + 1, y - 1
        while e < len(board) and f >= 0:
            if board[e][f] == "Q":
                return True 
            e, f = e + 1, f - 1

        return False 
'''
