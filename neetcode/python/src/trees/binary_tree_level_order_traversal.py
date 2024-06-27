from src.trees.treenode import TreeNode
from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            # only pop nodes in the current level
            level = []
            nodesInLevel = len(queue)
            # run bfs
            for i in range(nodesInLevel):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)

        return res
