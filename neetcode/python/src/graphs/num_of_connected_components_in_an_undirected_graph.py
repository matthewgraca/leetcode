from typing import List

class Solution:
    def __init__(self):
        pass

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency map from edges
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        unionVisit = set()
        componentCount = 0
        # visit every node
        for node in adj:
            visit = set()
            if node not in unionVisit:
                self.dfs(-1, node, adj, visit)
                # if a node can't be found in the union, it's a different component
                if not unionVisit & visit:
                    componentCount += 1
                unionVisit |= visit
        return componentCount 

    def dfs(self, prevNode: int, currNode: int, adj: dict, visit: set) -> None:
        if currNode in visit:
            return 

        visit.add(currNode)
        for nextNode in adj[currNode]:
            if prevNode != nextNode:
                self.dfs(currNode, nextNode, adj, visit)
        
        return

'''
this is just union-find
run dfs on the adjacency matrix starting at every node
if the set of visited nodes ever intersects, they are a group
    - if they don't intersect, increment count

i could memorize the bespoke union find solution, but spamming dfs is better honestly
'''
