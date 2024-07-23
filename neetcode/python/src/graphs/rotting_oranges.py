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
                    if self.indexInRange(grid, row, col) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1

        # need to account for when there are still fresh oranges remaining. set?
        return time if not fresh else -1

    def indexInRange(self, grid: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])
'''
all adjacent cells rotting at once implies a bfs

we need to gather all the places with a rotten orange, then propagate them
at once.
    - loop and find all rotten orange positions
    - do bfs, swapping adjacent 2s -> 1s
'''

'''
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    queue.append((r, c - 1))
                    fresh -= 1
                if c + 1 < cols and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    queue.append((r, c + 1))
                    fresh -= 1
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    queue.append((r - 1, c))
                    fresh -= 1
                if r + 1 < rows and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    queue.append((r + 1, c))
                    fresh -= 1
'''
