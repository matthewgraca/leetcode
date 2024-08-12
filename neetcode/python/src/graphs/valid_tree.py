from typing import List

class Solution:
    def __init__(self):
        pass

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adjacency list from the list of edges; create undirected graph
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # run dfs arbitrarily at node 0; we're just checking for two things:
        # 1. cycles
        # 2. connected
        # for both, where we start in an undirected graph doesn't matter
        visit = set()
        return self.dfs(-1, 0, adj, visit) and len(visit) == n
        
    # dfs that returns false if an undirected graph contains a cycle, true if not
    def dfs(self, prev: int, curr: int, adj: dict, visit: set) -> bool:
        if curr in visit:
            return False
        
        visit.add(curr)
        for neighbor in adj[curr]:
            # adjacent nodes aren't considered cycles, so skip them
            if prev != neighbor and not self.dfs(curr, neighbor, adj, visit):
                return False

        return True
