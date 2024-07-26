from typing import List

class Solution:
    def __init__(self):
        pass

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i : [] for i in range(n)}
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        visited = set()
        return self.dfs(-1, 0, adjMap, visited) and n == len(visited)

    def dfs(self, prevNode: int, currNode: int, adjMap: dict, visited: set) -> bool:
        # if already visited, then a cycle exists; return False
        if currNode in visited:
            return False

        visited.add(currNode)
        for neighbor in adjMap[currNode]:
            # we allow neighbors to point back to prev node, but not cycles
            if prevNode != neighbor:
                if not self.dfs(currNode, neighbor, adjMap, visited):
                    return False

        return True


'''
I assume that by "valid tree", they mean a graph with no cycles?
i think it may be as simple as dfs on the adjacency matrix with a visited
set.

after a valid path is written, we can delete that path to prevent retreading
already valid paths

the annoying thing is the nested list contains the node itself as well;
so this is not a classic adjacency list with the index being the node,
rather simply a list that describes how the nodes are connected.

so the conditions for traversal:
    - it's ok if the prevNode is the same as the next node (not a cycle)
'''
