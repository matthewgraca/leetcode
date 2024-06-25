from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case: node is null
        if not root:
            return None
        
        # preorder (top-down) invert children
        # can also do post-order (bottom-up) inversion
        root.left, root.right = root.right, root.left

        # dfs
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 
