from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def isBalanced(self, root: TreeNode) -> bool:
        _, isBalanced = self.maxDepth(root)
        return isBalanced

    def maxDepth(self, root: TreeNode) -> (int, bool):
        if not root:
            return 0, True
        
        leftMaxDepth, isLeftTreeBalanced = self.maxDepth(root.left)
        rightMaxDepth, isRightTreeBalanced = self.maxDepth(root.right)

        # only balanced if all subtrees are balanced as well
        isBalanced = isLeftTreeBalanced and isRightTreeBalanced
        if abs(leftMaxDepth - rightMaxDepth) > 1:
            isBalanced = False

        return 1 + max(leftMaxDepth, rightMaxDepth), isBalanced
