from typing import List
from collections import deque

class TreeNode:
    class TreeNode:
        pass

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # takes a list and creates a binary tree of it
    #         i
    #       /   \
    #     2i+1 2i+2
    def treeOf(self, nodelist: List[int]) -> TreeNode:
        return self.buildTree(0, nodelist)

    def buildTree(self, i: int, nodelist: List[int]) -> TreeNode:
        if i >= len(nodelist):
            return None

        return TreeNode(
                    val=nodelist[i], 
                    left=self.buildTree(2*i+1, nodelist), 
                    right=self.buildTree(2*i+2, nodelist)
                )

    # takes a node and creates a list in the form:
    #         i
    #       /   \
    #     2i+1 2i+2
    def listOf(self, root: TreeNode) -> List[int]:
        res = []
        self.bfs(root, res)
        return res

    # simple dfs, no cycles
    def dfs(self, node: TreeNode, res: List[int]):
        # base case: leaf node
        if not node:
            return

        res.append(node.val)
        # go left; when exhausted, go right
        self.dfs(node.left, res)
        self.dfs(node.right, res)

    # simple bfs, no cycles
    def bfs(self, node: TreeNode, res: List[int]):
        # empty case
        if not node:
            return

        # nonempty case
        queue = deque() 
        queue.append(node)
        while queue:
            temp = queue.popleft()
            res.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
