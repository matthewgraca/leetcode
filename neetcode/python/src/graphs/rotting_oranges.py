from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # gather position of all rotting oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                # place all rotting oranges in bfs queue
                if grid[row][col] == 2:
                    queue.append((row, col))

        # run bfs on every rotting orange at the same time
        # but exit if no fresh oranges remain to avoid overcounting time
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        time = 0
        while fresh > 0 and queue:
            # propagate rot for current level
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # in range and fresh -> propagate rot
                    if self.promising(grid, row, col):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1

        # need to account for when there are still fresh oranges remaining. set?
        return time if not fresh else -1

    def promising(self, grid: List[List[int]], row: int, col: int) -> bool:
        return (
            row >= 0 and col >= 0 and 
            row < len(grid) and col < len(grid[0]) and
            grid[row][col] == 1
        )

