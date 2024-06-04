from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init__(self):
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.slicing(preorder, inorder)

    def slicing(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        # get the root of the subtree from preorder, 
        # and the index which root appears in inorder 
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        midIdx = inorder.index(rootVal)

        # slices that contain left and right subtrees
        root.left = self.slicing(preorder[1 : midIdx+1], inorder[0 : midIdx])
        root.right = self.slicing(preorder[midIdx+1 :], inorder[midIdx+1 :])

        return root 
'''
This is a bit easier to conceptualize when you write out the relationship 
between inorder and preorder traversal. There are two key ideas:
    1. relationship b/t the two traversals
    2. the recursive solution

First, it's worth remembering the traversal invariants:
    - preorder: root, left, right
    - inorder: left, root, right
From these invariants, we can determine the structure of the the binary tree 
with clever indexing.

So using the two orders, we can construct what the root node is, and 
what values lie in the left and right subtrees of this root node.
    - preorder[0] is the root node.
    - mid = inorder.index(preorder[0]) is the index where the root is; call it mid

So, what do we currently know?
    - We know that every value to the right of preorder[0] is in the left and 
        right subtree; but not exactly where.
    - We know that every value to the left of inorder[mid] is in the left 
        subtree, and every value to the right of inorder[mid] is in the 
        right subtree.

So to finish this off, we need to know where preorder splits from right subtree 
to left subtree.
    - If the order of inorder is left-root-right and the order of preorder 
        is root-left-right, then the mid index tells us where left and right 
        split in preorder. See image I made

time:
    O(n^2)
        - it's kind of nebulous; ideally we slice the array in half for the left 
        and the other half for the right for a total of n time, but at each split
        we need to do an n scan for the index where the root value appears in 
        inorder. so the total is n splits, n scan per split, so O(n^2)
        - there's a solution with a hashmap, but then the indexing becomes complicated
        because at every slice, the structure of the inorder array changes, so just
        building one hashmap is insufficient. the complexity of the indexing just
        isn't worth figuring out mid-interview.
space:
    only a constant amount of space is used
'''
