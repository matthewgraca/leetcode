from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def isSameTree(self, p: TreeNode, q: TreeNode)-> bool:
        # case 1: both null
        if not p and not q:
            return True
        # case 2: one is null, but not the other
        if not p or not q:
            return False

        # recursive step: both are nodes and are equal val
        isRootValSame = p.val == q.val
        isLeftTreeSame = self.isSameTree(p.left, q.left)
        isRightTreeSame = self.isSameTree(p.right, q.right)

        return isRootValSame and isLeftTreeSame and isRightTreeSame
