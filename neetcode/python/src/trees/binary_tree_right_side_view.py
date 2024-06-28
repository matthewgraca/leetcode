from src.trees.treenode import TreeNode
from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # level order traversal
        res = []
        q = deque([root])
        while q:
            # top of queue will contain rightmost node on the current level
            res.append(q[0].val)
            nodesInLevel = len(q)
            for _ in range(nodesInLevel):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
