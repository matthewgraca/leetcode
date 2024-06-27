from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def lowestCommonAncestorIt(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # binary search for p and q
        while True:
            # if p and q are left, go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # if p and q are right, go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # if p and q are in between root (or one is equal to root), return
            else:
                return root

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # p and q guaranteed to be in tree, so no real base case needed

        # recursive step:
        # go left if p and q are left
        if p.val < root.val and q.val < root.val:
            root = self.lowestCommonAncestor(root.left, p, q)
        
        # go right if p and q are right
        if p.val > root.val and q.val > root.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        
        # when lca is found, return root 
        # ((p>root>q) or (p<root<q) or (p=root or q=root))
        return root
