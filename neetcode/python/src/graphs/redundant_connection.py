from typing import List

class Solution:
    def __init__(self):
        pass

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        adj = {i : [] for i in range(1, len(edges) + 1)}
        for a, b in edges:
            if self.dfs(0, a, b, adj):
                res = [a, b]
            else:
                adj[a].append(b)
                adj[b].append(a)
        return res
    
    # runs dfs on the target node to detect a cycle
    def dfs(
        self, 
        prev: int, 
        curr: int, 
        target: int, 
        adj: dict 
    ) -> bool:
        # cycle found 
        if curr == target:
            return True 
        
        # dfs check neighbors
        for neighbor in adj[curr]:
            if neighbor != prev:
                if self.dfs(curr, neighbor, target, adj):
                    return True

        # no cycle found
        return False


'''
another example of just ignoring union find and running dfs LMAO
notes:
    The idea here is that we build the adjacency list edge by edge.
    For each edge, we run dfs from the source to the target. we fix the target,
        and run dfs and check every neighbor of the source to see if they reach
        the target.

        If the neighbors can reach the target (without going through the previous
        source), that means that a cycle was created, and we exit.

        If no neighbor can meet the target (without going through the source), then
        there's no cycle. We add that edge to the adjacency list

    This means that the moment a cycle is created, we can detect which edge would
    create that cycle; allowing us to return the specific edge that would create 
    that cycle.

time: 
    dfs takes time proportional to the number of verticies. we run dfs for 
    a potential max of n times. however, it is run on an adjacency list
    that grows from 1 to n -- so it looks like this:
        1 * 1 + 1 * 2 + 1 * 3 + ... + 1_n * n = 1 + 2 + ... + n = n^2
'''
