from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init__(self):
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # base case: arrays sliced to the bone
        if not preorder or not inorder:
            return None

        # get the root of the subtree from preorder, 
        root = TreeNode(preorder[0])
        midIdx = inorder.index(preorder[0])
        # recall syntax: [a,b) = [a,b+1] and [a:] = [a:len(list)]
        root.left = self.buildTree(preorder[1 : midIdx+1], inorder[0 : midIdx])
        root.right = self.buildTree(preorder[midIdx+1 :], inorder[midIdx+1 :])

        return root 
