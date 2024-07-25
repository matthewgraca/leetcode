from typing import List

class Solution:
    def __init__(self):
        pass

    def solve(self, board: List[List[str]]) -> None:
        # any regions that start on a border are unsurroundable
        # thus if any "O"s are on the border, 
        # use dfs to get the region and mark them "U"
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.isBorderIndex(board, row, col) and board[row][col] == "O":
                    self.dfs(board, row, col)

        # re-mark regions
        for row in range(rows):
            for col in range(cols):
                # surroundable regions kept their "O". flip them to "X"
                if board[row][col] == "O":
                    board[row][col] = "X"
                # unsurroundable regions marked with "U". flip them back to "O"
                if board[row][col] == "U":
                    board[row][col] = "O"

        return

    def dfs(
        self,
        board: List[List[str]],
        r: int,
        c: int
    ) -> None:
        # not in range, visited, or not a region: backtrack
        if not self.validNode(board, r, c):
            return 

        board[r][c] = "U"
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for dr, dc in directions:
            row, col = r + dr, c + dc
            self.dfs(board, row, col)

        return 

    def validNode(
        self, 
        board: List[List[str]], 
        row: int, 
        col: int
    ) -> bool:
        # in range, not visited, and is a region ("O")
        return(
            row >= 0 and row < len(board) and
            col >= 0 and col < len(board[0]) and
            board[row][col] == "O"
        )

    def isBorderIndex(self, board: List[List[str]], row: int, col: int) -> bool:
        return(
            row == 0 or col == 0 or 
            row == len(board) - 1 or col == len(board[0]) - 1
        )
'''
my initial guess is to run bfs on the X nodes.
    - if surrounded by Xs, then capture
    - if has an adjacent O, check it
need a "surrounded" condition?
    - I think we can ignore the border b/c they are not surroundable
    - so if our bfs ends with an O on an edge, then the region is not surroundable

another idea is to run dfs to collect all the Os in a region. once all the Os hae been exhausted,
    we backtrack and check the nodes if they are surrounded?
    - that way if a region ever goes in contact with the border, we just abort and mark the region
        as not surroundable?
    - if we do dfs and a neighbor has been visited (but isn't an X), does that mean
        this node is by default not surroundable? Because if was visited and didn't 
        change to X, then it touches a node that's at the edge?? so we just mark it 
        as not surroundable?


okay seeing some lessons here. if you are adding a visit set, make sure to add the node 
before the recursive call

also if you are doing the for loop to change direction indices, use a new local variable
(in this case, row instead of r)
'''
