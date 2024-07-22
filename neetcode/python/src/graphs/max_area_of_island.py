from typing import List

class Solution:
    def __init__(self):
        pass

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxCount = max(maxCount, self.dfs(grid, row, col))
        return maxCount

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        rows, cols = len(grid), len(grid[0])
        # if not in-bound, backtrack
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        # if not an island or already visited, backtrack
        if grid[row][col] == 0:
            return 0

        # dfs; mark current node as visited
        grid[row][col] = 0
        count = 1 + (
            self.dfs(grid, row - 1, col) +
            self.dfs(grid, row + 1, col) +
            self.dfs(grid, row, col - 1) +
            self.dfs(grid, row, col + 1)
        )

        return count
