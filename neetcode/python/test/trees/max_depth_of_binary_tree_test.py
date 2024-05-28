import unittest
from src.trees.treenode import TreeNode
from src.trees.max_depth_of_binary_tree import Solution

class MaxDepthOfBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = [3,9,20,None,None,15,7]
        actual = Solution().maxDepth(TreeNode().treeOf(root))
        expected = 3
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [1,None,2]
        actual = Solution().maxDepth(TreeNode().treeOf(root))
        expected = 2
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = []
        actual = Solution().maxDepth(TreeNode().treeOf(root))
        expected = 0
        self.assertEqual(actual, expected)
