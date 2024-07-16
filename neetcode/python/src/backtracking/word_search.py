from typing import List

class Solution:
    def __init__(self):
        pass

    def exist(self, board: List[List[int]], word: str) -> bool:
        return self.checkNode(board, 0, 0, 0, word) 

    def checkNode(
        self,
        board: List[List[int]],
        i: int,
        x: int,
        y: int,
        word: str
    ) -> bool:
        m, n = len(board), len(board[0])
        # solution found: word scan completed
        if i == len(word):
            return True 

        # check curr node
        if self.validNode(i, x, y, board, word):
            visitedNode = board[x][y]
            # check neighbors
            validNeighbor = (
                self.checkNode(board, i+1, x+1, y, word) or
                self.checkNode(board, i+1, x, y+1, word) or 
                self.checkNode(board, i+1, x, y-1, word) or
                self.checkNode(board, i+1, x-1, y, word) 
            )
            # path from x,y failed; backtrack and unvisit nodes
            board[x][y] = visitedNode
            return validNeighbor
        # invalid node or no solution; backtrack
        return False 

    # determine if a node is valid
    def validNode(
        self, 
        i: int,
        x: int, 
        y: int, 
        board: List[List[int]], 
        word: str
    ) -> bool:
        # in bounds and letter found and not visited, it's a valid node
        m, n = len(board), len(board[0])
        inBounds = x < m and y < n and x >= 0 and y >= 0
        if inBounds and board[x][y] == word[i] and not board[x][y] == "":
            board[x][y] = "" # mark node as visited
            return True
        return False

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
