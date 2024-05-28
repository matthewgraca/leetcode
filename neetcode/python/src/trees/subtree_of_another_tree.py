from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init_(self):
        pass

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # find all nodes that share the same root as the subtree using dfs
        st = [root]
        while st:
            node = st.pop()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)

        return False

    # determines if one tree is the same tree as another
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # same structure base case
        if not p and not q:
            return True
        # different structure
        if p and not q or q and not p:
            return False

        # check if current node is the same and left + right trees are the same
        isSameNode = p.val == q.val
        isSameLeftTree = self.isSameTree(p.left, q.left)
        isSameRightTree = self.isSameTree(p.right, q.right)

        return isSameNode and isSameLeftTree and isSameRightTree

'''
important distinction to be made is all the descendants also have to be the same;
if tree A has tree B in it, but the descendants are different, they aren't the same
    1. search for the root of subtree in the tree
    2. if found, check if same tree
        - if same tree return true
        - if not, return false
    3. if not found, return true
'''
