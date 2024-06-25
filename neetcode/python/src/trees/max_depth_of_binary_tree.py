from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # postorder traversal, save only deepest value
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
