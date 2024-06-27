from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def diameterOfBinaryTree(self, root: TreeNode)-> int:
        _, diameter = self.depthAndDiameter(root)
        return diameter

    def depthAndDiameter(self, root: TreeNode) -> (int, int):
        if not root:
            return 0, 0
        
        # get current max depth and diameter of this node
        leftTreeMaxDepth, leftTreeDiameter = self.depthAndDiameter(root.left)
        rightTreeMaxDepth, rightTreeDiameter = self.depthAndDiameter(root.right)

        # calculate new max depth and diameter
        maxDepth = max(leftTreeMaxDepth, rightTreeMaxDepth) + 1
        # note : we don't add 1 b/c of the definition of diameter counts edges, not nodes
        currDiameter = leftTreeMaxDepth + rightTreeMaxDepth
        maxDiameter = max(leftTreeDiameter, rightTreeDiameter, currDiameter)

        # pass those values up during post-order traversal
        return maxDepth, maxDiameter
