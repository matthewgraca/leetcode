from typing import List

class Solution:
    def __init__(self):
        pass

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedPacific, visitedAtlantic = set(), set()
        rows, cols = len(heights), len(heights[0])

        # traverse coastal nodes
        pacificRow, pacificCol = 0, 0
        atlanticRow, atlanticCol = rows - 1, cols - 1 
        for col in range(cols):
            self.dfs(heights, pacificRow, col, heights[pacificRow][col], visitedPacific)
            self.dfs(heights, atlanticRow, col, heights[atlanticRow][col], visitedAtlantic)
        for row in range(rows):
            self.dfs(heights, row, pacificCol, heights[row][pacificCol], visitedPacific)
            self.dfs(heights, row, atlanticCol, heights[row][atlanticCol], visitedAtlantic)

        # intersect sets and convert to 2d list
        visitedBothOceans = visitedPacific & visitedAtlantic
        res = []
        for a, b in visitedBothOceans:
            res.append([a, b])

        return res 

    def dfs(
        self,
        heights: List[List[int]],
        row: int,
        col: int,
        prevHeight: int,
        visited: set
    ) -> None:
        # invalid node: backtrack
        if not self.validNode(heights, row, col, prevHeight, visited):
            return

        # dfs visit neighbors
        visited.add((row, col))
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            self.dfs(heights, r, c, heights[row][col], visited)

        # all neigbors checked; backtrack
        return

    def validNode(
        self, 
        heights: List[List[int]], 
        row: int, 
        col: int,
        nodeVal: int,
        visited: set
    ) -> bool:
        if (row, col) in visited:
            return False
        if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
            return False
        if heights[row][col] < nodeVal:
            return False

        # neighbor: not visited, within range of matrix, and is elevated
        return True

'''
this is a graph problem -- abstract this matrix into a graph problem.

looks like we're being asked to perform some sort of either bfs or dfs
with the rainwater at each coordinate? We search given the following conditions:
    1. atlantic is found; look for pacific
    2. pacific is found; look for atlantic
    3. both are found; return true?
    4. either only one or none are found; return false.

map{(r,c): bool}
    - bool is if the coordinate reaches the pacific
    - if it does, we can try to go to those coordinants and check if they go 
        to the atlantic; there's no point in checking if the coords that can't 
        go to the pacific are able to go to the atlantic since we're looking for
        coords that do both.

idea: instead of picking a coordinate and going down towards the ocean,
instead can we pick the coordiantes at the borders and attempt to go up?
if we can, all teh coordinants that get caught in the path are valid.
    - every node that gets visited gets put in a set -- that marks 
    that they have both already been visited, and that they already have 
    a valid path to the ocean.


programmatically:
    1. traverse the nodes that are directly adjacent (coastal nodes) to the pacific
        - add the visited node to the set of visited nodes
        - run dfs/bfs. continue if an adjacent node is greater than or equal to the 
        current node; else backtrack.
        - continue until all coastal nodes have performed the search.
    2. do the same for the atlantic coastal nodes.
    3. intersect the pacific and atlantic sets -- this is the answer.
'''
