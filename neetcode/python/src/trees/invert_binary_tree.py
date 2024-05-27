from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case: node is null
        if not root:
            return None
        
        # swap left and right children 
        root.left, root.right = root.right, root.left

        # dfs
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 
'''
complexity:
    time: each node is visited once: so if there are n nodes, the answer is O(n)
    space: O(h), where h is the depth of the tree, or h nodes in memory for the deepest node
'''
