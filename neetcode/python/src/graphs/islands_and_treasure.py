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

'''
bfs to find closest treasure cell from each land cell

to flip this, we run bfs from the treasure and mark each
land cell by +1 after each level of bfs

I thought that you would need to pick up the min distance and mess with 
the visited set, but it turns out that since the bfs occurs from all the 
treasure cells at the same time, the searches end up "meeting" each other,
instead of one overlapping the other search. so there's no need to save the 
smallest distance since the searches are done concurrently 

Let mn be the size of the grid
time: 
    - mn to search for treasure cells and push relevant cells into queue
    - worst case mn time searching every cell
    - O(mn)
space:
    - queue worst case becomes mn size
    - visiting every node means set becomes mn size
    - O(mn)
'''
