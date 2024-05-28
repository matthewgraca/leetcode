from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxDepth, diameter = self.maxDepthAndDiameter(root)
        return diameter

    def maxDepthAndDiameter(self, root: TreeNode) -> (int, int):
        if root is None:
            return 0, 0

        # get the depth and diameter of the left tree
        leftTreeDepth, leftTreeDiameter = self.maxDepthAndDiameter(root.left)
        # get the depth and diameter of the right tree
        rightTreeDepth, rightTreeDiameter = self.maxDepthAndDiameter(root.right)
        # sum left and right tree depth at current moment for a current diameter
        currentDiameter = leftTreeDepth + rightTreeDepth
        # the max diameter is the largest diameter of the three
        maxDiameter = max(leftTreeDiameter, rightTreeDiameter, currentDiameter)

        return max(leftTreeDepth, rightTreeDepth) + 1, maxDiameter 
'''
The idea is the diameter of a binary tree is the sum of the max left tree depth and the max right tree depth.
    - this means we need to save both the max depth of the current tree, and the total diameter at this moment.

Some solutions opt to use a global diameter state, but i want this to be as stateless as possible since leetcode may create an object out of this class, essentially reusing diameter, which saves the last largest diameter of a different tree.

complexity:
    time: O(n) for n nodes
    space: O(n) for n nodes (for a degenerate binary tree)
'''
