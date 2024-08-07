from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasureCell, waterCell = 0, -1
        rows, cols = len(grid), len(grid[0])

        # push all the cells that will use bfs into the queue
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == treasureCell:
                    queue.append((row, col))

        # run bfs from treasure cells to land cells
        distance = 1 
        visited = set()
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if self.validNode(grid, row, col, visited): 
                        visited.add((row, col))
                        grid[row][col] = distance 
                        queue.append((row, col))

            distance += 1

        return

    # valid if in range and a land cell, and not visited
    def validNode(
        self,
        grid: List[List[int]], 
        row: int, 
        col: int, 
        visited: set
    ) -> bool:
        treasureCell, waterCell = 0, -1
        return(
            row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and
            (row, col) not in visited and
            grid[row][col] != waterCell and grid[row][col] != treasureCell 
        )
