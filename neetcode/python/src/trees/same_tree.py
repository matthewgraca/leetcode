from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

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
Two criteria:
    1. structurally identitcal
    2. nodes have the same value

seems like we can pick our choice in dfs or bfs and just do a 
pairwise comparison?
'''
