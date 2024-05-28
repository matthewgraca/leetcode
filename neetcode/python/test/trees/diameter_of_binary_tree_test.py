import unittest
from src.trees.treenode import TreeNode
from src.trees.diameter_of_binary_tree import Solution

class DiameterOfBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = [1,2,3,4,5]
        actual = Solution().diameterOfBinaryTree(TreeNode().treeOf(root))
        expected = 3
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [1,2]
        actual = Solution().diameterOfBinaryTree(TreeNode().treeOf(root))
        expected = 1
        self.assertEqual(actual, expected)
