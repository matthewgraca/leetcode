from typing import List

class Solution:
    def __init__(self):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        # run dfs to swap all 1s to 0s
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        if not self.promising(grid, row, col):
            return
        
        grid[row][col] = "0"
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            self.dfs(grid, r, c)
        
        return

    def promising(self, grid: List[List[str]], row: int, col: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        return (
            # in range
            row >= 0 and col >= 0 and 
            row < ROWS and col < COLS and
            # cell is an island
            grid[row][col] == "1"
        )
