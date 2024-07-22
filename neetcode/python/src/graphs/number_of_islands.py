from typing import List

class Solution:
    def __init__(self):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], row: int, col: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # if out of bounds, backtrack
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 
        # if the current position is 0, it's sea or visited; backtrack
        if grid[row][col] == "0":
            return 

        # mark current position as visited (sea)
        grid[row][col] = "0" 
        # dfs search
        self.dfs(grid, row + 1, col) 
        self.dfs(grid, row - 1, col) 
        self.dfs(grid, row, col + 1) 
        self.dfs(grid, row, col - 1)

        return # island found
'''
idea: use dfs to search for all 1s connected together
once the search is over, we flip all the 1s we found to 0 (to indicate it was visited)
'''
