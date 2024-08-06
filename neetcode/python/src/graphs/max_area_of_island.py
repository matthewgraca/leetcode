from typing import List

class Solution:
    def __init__(self):
        pass

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount = 0
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxCount = max(self.dfs(grid, row, col), maxCount)
        return maxCount

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int:
        if not self.promising(grid, row, col):
            return 0
        
        grid[row][col] = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 1
        for dr, dc in directions:
            r, c = row + dr, col + dc
            count += self.dfs(grid, r, c)
        
        return count

    def promising(self, grid: List[List[int]], row: int, col: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        return (
            # indices in range
            row >= 0 and col >= 0 and
            row < ROWS and col < COLS and
            # island encountered
            grid[row][col] == 1
        )
