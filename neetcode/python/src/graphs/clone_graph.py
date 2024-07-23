from src.graphs.node import Node

class Solution:
    def __init__(self):
        pass

    def cloneGraph(self, node: Node) -> Node:
        # maps old graph to copied graph nodes
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, node: Node, visited: dict) -> Node:
        # base case: null returns null
        if not node:
            return None
        # if already visited, backtrack
        if node in visited:
            return visited[node]

        # preorder traversal - make copy
        copy = Node(node.val)
        visited[node] = copy

        # dfs on neighbors
        for edge in node.neighbors:
            copy.neighbors.append(self.dfs(edge, visited))

        # return copy after all neighbors copied
        return copy

'''
This looks like copy list with random pointer;
needing a hashmap to follow how each node points to others
'''
