from src.trees.treenode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    # depth first search that also remembers the largest ancestor's value
    def dfs(self, root: TreeNode, maxVal: int) -> int:
        if not root:
            return 0

        # maxVal is the largest value between the current node and the root (pre-order traversal)
        # if the node is >= the max value of its ancestors, increment count of good node
        count = 1 if root.val >= maxVal else 0

        maxVal = max(maxVal, root.val) 
        count += self.dfs(root.left, maxVal)
        count += self.dfs(root.right, maxVal)

        return count
