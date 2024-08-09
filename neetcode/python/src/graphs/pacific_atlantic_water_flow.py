from typing import List

class Solution:
    def __init__(self):
        pass

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # scan edges for which cells connect to their edge
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for col in range(COLS):
            self.dfs(heights, 0, col, pacific)
            self.dfs(heights, ROWS - 1, col, atlantic)
        for row in range(ROWS):
            self.dfs(heights, row, 0, pacific)
            self.dfs(heights, row, COLS - 1, atlantic)
        
        # intersection of pacific and atlantic sets is the result
        res = []
        for a, b in pacific & atlantic:
            res.append([a, b])

        return res

    def dfs(self, heights: List[List[int]], row: int, col: int, visit: set) -> None:
        visit.add((row, col))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.promising(heights, heights[row][col], r, c, visit):
                self.dfs(heights, r, c, visit)
        
        return

    def promising(self, heights: List[List[int]], curr: int, row: int, col: int, visit: set) -> bool:
        ROWS, COLS = len(heights), len(heights[0])
        return (
            # indices within range
            row >= 0 and col >= 0 and
            row < ROWS and col < COLS and
            # cell not visited already
            (row, col) not in visit and
            # adjacent val >= curr val
            heights[row][col] >= curr
        )
