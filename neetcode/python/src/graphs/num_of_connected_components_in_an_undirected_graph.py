from typing import List

class Solution:
    def __init__(self):
        pass

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list in the form of an undirected graph
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # run dfs to find all connected components
        visit = set()
        count = 0
        for node in adj:
            # dfs visits all nodes connected to the given node
            if node not in visit:
                self.dfs(-1, node, adj, visit)
                count += 1
        
        return count
        
    def dfs(self, prev: int, curr: int, adj: dict, visit: set) -> None:
        # cycle detected; backtrack
        if curr in visit:
            return
            
        # keep track of every node we visit
        visit.add(curr)
        for neighbor in adj[curr]:
            if prev != neighbor:
                self.dfs(curr, neighbor, adj, visit)

        # no neighbors; backtrack
        return
