from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def maxPathSum(self, root: TreeNode) -> int:
        _, maxPath = self.dfs(root)
        return maxPath

    # returns (current sum path, max sum path)
    def dfs(self, root: TreeNode) -> (int, int):
        if not root:
            return 0, float('-inf')

        # generate left and right path, ignore paths with negative numbers
        leftTreePath, maxLeftTreePath = self.dfs(root.left)
        leftTreePath = max(leftTreePath, 0)
        rightTreePath, maxRightTreePath = self.dfs(root.right)
        rightTreePath = max(rightTreePath, 0)

        # by post order traversal:
        # calculate the globally max path
        currPath = leftTreePath + rightTreePath + root.val
        maxPath = max(maxLeftTreePath, maxRightTreePath, currPath)

        # traversing up the tree: pass in the best path b/t left and right
        maxCurrPath = max(leftTreePath, rightTreePath) + root.val

        return maxCurrPath, maxPath 
