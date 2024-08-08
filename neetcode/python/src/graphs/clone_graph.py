from src.graphs.node import Node

class Solution:
    def __init__(self):
        pass

    def cloneGraph(self, node: Node) -> Node:
        return self.dfs(node, {})
        
    def dfs(self, org: Node, orgToCopy: dict) -> Node:
        # empty graph -- return None
        if org is None:
            return None
        
        # copy already made; return the copy
        if org in orgToCopy:
            return orgToCopy[org]
        
        # create copy and visit neighbors
        copy = Node(org.val)
        orgToCopy[org] = copy
        for neighbor in org.neighbors:
            copy.neighbors.append(self.dfs(neighbor, orgToCopy))
        
        return copy
