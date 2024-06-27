from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init_(self):
        pass

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # dfs to compare trees at every node
        # case 1: subRoot is null; trivially a subtree of root
        if not subRoot:
            return True
        # case 2: subRoot contains more nodes than root; can't be a subtree
        if not root:
            return False
        # case 3: trees are the same at current root
        if self.isSameTree(root, subRoot):
            return True

        # recursive step -- check left and right subtrees
        isLeftTreeSameAsSubtree= self.isSubtree(root.left, subRoot)
        isRightTreeSameAsSubtree = self.isSubtree(root.right, subRoot)

        return isLeftTreeSameAsSubtree or isRightTreeSameAsSubtree

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        isLeftTreeSame = self.isSameTree(p.left, q.left)
        isRightTreeSame = self.isSameTree(p.right, q.right)

        return isLeftTreeSame and isRightTreeSame
