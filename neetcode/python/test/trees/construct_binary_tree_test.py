import unittest
from src.trees.treenode import TreeNode
from src.trees.construct_binary_tree import Solution

class ConstructBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
        actual = TreeNode().listOf(
                Solution().buildTree(preorder, inorder)
            )
        expected = TreeNode().listOf(
                TreeNode().treeOf([3,9,20,None,None,15,7])
            )
        self.assertEqual(actual, expected)

    def test_example2(self):
        preorder, inorder = [-1], [-1]
        actual = TreeNode().listOf(
                Solution().buildTree(preorder, inorder)
            )
        expected = TreeNode().listOf(
                TreeNode().treeOf([-1])
            )
        self.assertEqual(actual, expected)

