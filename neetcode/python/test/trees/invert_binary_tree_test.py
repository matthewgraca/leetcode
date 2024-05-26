import unittest
from src.trees.treenode import TreeNode
from src.trees.invert_binary_tree import Solution

class InvertBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = TreeNode().treeOf([1,2,3,4,5,6,7])
        actual = TreeNode().listOf(Solution().invertTree(root))
        expected = [1,3,2,7,6,5,4]
        self.assertEqual(actual, expected)
