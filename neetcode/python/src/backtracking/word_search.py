from typing import List

class Solution:
    def __init__(self):
        pass

    def exist(self, board: List[List[int]], word: str) -> bool:
        # check every path starting from (i,j)
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if self.checkNode(board, word, 0, i, j):
                    return True
        return False

    # checks if a path starting from x,y is valid
    def checkNode(
        self,
        board: List[List[int]],
        word: str,
        i: int,
        x: int,
        y: int
    ) -> bool:
        m, n = len(board), len(board[0])
        # solution found: word scan completed
        if i == len(word):
            return True 

        # check curr node
        if self.validNode(board, word, i, x, y):
            visitedNode = board[x][y]
            board[x][y] = "" # mark node as visited
            # check neighbors
            validNeighbor = (
                # right, down, left, up
                self.checkNode(board, word, i+1, x+1, y) or
                self.checkNode(board, word, i+1, x, y+1) or 
                self.checkNode(board, word, i+1, x-1, y) or
                self.checkNode(board, word, i+1, x, y-1) 
            )
            # path from x,y failed; backtrack and unvisit nodes
            board[x][y] = visitedNode
            return validNeighbor
        # invalid node or no solution; backtrack
        return False 

    # determine if a node is valid
    def validNode(
        self, 
        board: List[List[int]], 
        word: str,
        i: int,
        x: int, 
        y: int
    ) -> bool:
        m, n = len(board), len(board[0])
        return(
            x < m and y < n and x >= 0 and y >= 0 and # indices in-bounds
            board[x][y] == word[i] # letter in word matches letter on board
        )

'''
ideas:
    - need to check the values adjacent to the current value; but do NOT go to where you came from
        - say a for loop or whatever we can do to check adjacents; maybe eafch node can have a "visited" state?
    - solution: subword length == word length
    - basically an adjacency matrix we go dfs on; so we will need some idea of "visited" nodes.
backtracking
    -sequence from a set based on a criteria
    -when backtrack: no valid adjacent, non-visited letters
visited:
    - map of ordered pair? e.g. (0,0) -> True ? or perhaps just a set; if the pair is in the set it's
        visited, if it's not then their pair hasn't been visited.
        - need a dictionary, since there are duplicate letters


What is a neighbor?
for (x,y)
    -right (x+1,y)
    -up (x,y+1)
    -down (x, y-1)
    -left (x-1, y)
'''
