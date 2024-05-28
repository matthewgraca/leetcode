from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def isBalanced(self, root: TreeNode) -> bool:
        maxDepth, isTreeBalanced = self.maxDepth(root)
        return isTreeBalanced

    def maxDepth(self, root: TreeNode) -> (int, bool):
        if not root:
            return 0, True

        # get depth of left and right tree, along with if it was balanced
        leftTreeDepth, isLeftBalanced = self.maxDepth(root.left)
        rightTreeDepth, isRightBalanced = self.maxDepth(root.right)

        # check the current balance
        isCurrBalanced = False if abs(leftTreeDepth - rightTreeDepth) > 1 else True

        # tree is balanced only if it was, and is, balanced (at every node)
        isTotalBalanced = isLeftBalanced and isRightBalanced and isCurrBalanced

        return max(leftTreeDepth+1, rightTreeDepth+1), isTotalBalanced
        
'''
The definition of a balanced tree is that it is "height-balanced"; i.e., the depth 
of two subtrees of EVERY node never differs by more than one.
    - so it's not just comparing the left and right subtree from the root;
        you have to compare the left and right subtree depth at EVERY node

So the idea is to get the left subtree depth and the rigth subtree depth for each node. If the 
difference is more than 1, return false
'''
