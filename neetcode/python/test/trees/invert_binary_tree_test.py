import unittest
from src.trees.treenode import TreeNode
from src.trees.invert_binary_tree import Solution

class InvertBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = TreeNode().treeOf([1,2,3,4,5,6,7])
        actual = TreeNode().listOf(Solution().invertTree(root))
        expected = [1,3,2,7,6,5,4]
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = TreeNode().treeOf([4,2,7,1,3,6,9])
        actual = TreeNode().listOf(Solution().invertTree(root))
        expected = [4,7,2,9,6,3,1]
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = TreeNode().treeOf([2,1,3])
        actual = TreeNode().listOf(Solution().invertTree(root))
        expected = [2,3,1]
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = TreeNode().treeOf([])
        actual = TreeNode().listOf(Solution().invertTree(root))
        expected = []
        self.assertEqual(actual, expected)
