from src.trees.treenode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node: TreeNode, leftVal: int, rightVal: int) -> bool:
        if not node:
            return True
        if node.val <= leftVal or node.val >= rightVal:
            return False

        # go left: update upper bound; go right: update lower bound
        isLeftSubtreeValid = self.dfs(node.left, leftVal, node.val)
        isRightSubtreeValid = self.dfs(node.right, node.val, rightVal)

        return isLeftSubtreeValid and isRightSubtreeValid
