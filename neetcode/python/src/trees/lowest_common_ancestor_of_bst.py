from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # binary search for p and q
        while True:
            # if both p and q in left subtree, go there
            if p.val < root.val and q.val < root.val:
                root = root.left
            # elif both p and q in right subree, go there
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # a node was found, so the other must be a child of this node
            # or one is in the left tree and the other is in the right tree
            else:
                return root
'''
got sent to implementation hell because i forgot this was a BINARY SEARCH TREE
time:
    binary search for 2 valules, but done at the same time so just lgn
space:
    1
'''
