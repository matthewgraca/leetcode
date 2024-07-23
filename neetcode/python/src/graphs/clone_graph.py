from src.graphs.node import Node

class Solution:
    def __init__(self):
        pass

    def cloneGraph(self, node: Node) -> Node:
        # maps old graph to copied graph nodes
        originalToCopy = {}
        return self.dfs(node, originalToCopy) if node else None

    def dfs(self, node: Node, originalToCopy: dict) -> Node:
        # if already visited, backtrack
        if node in originalToCopy:
            return originalToCopy[node]

        # preorder traversal - make copy
        copy = Node(node.val)
        originalToCopy[node] = copy

        # dfs
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor, originalToCopy))

        return copy

'''
This looks like copy list with random pointer;
needing a hashmap to follow how each node points to others
'''
