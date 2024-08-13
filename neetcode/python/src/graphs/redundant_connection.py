from typing import List

class Solution:
    def __init__(self):
        pass

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # adjacency list from [1, n]
        adj = {i + 1 : [] for i in range(len(edges))}

        # run dfs as the adj list is built, edge by edge
        # if dfs finds a cycle, return the edge that made it
        for a, b in edges:
            if self.dfs(0, a, b, adj):
                return [a, b]
            else:
                adj[a].append(b)
                adj[b].append(a)
        
        return [0, 0]
        
    def dfs(self, prev: int, curr: int, target: int, adj: dict) -> bool:
        # cycle found
        if curr == target:
            return True
        
        # dfs check neighbors
        for neighbor in adj[curr]:
            if prev != neighbor and self.dfs(curr, neighbor, target, adj):
                return True

        return False
