import unittest
from src.trees.treenode import TreeNode
from src.trees.binary_tree_max_path_sum import Solution

class BinaryTreeMaxPathSumTest(unittest.TestCase):
    def test_example1(self):
        root = [1,2,3]
        actual = Solution().maxPathSum(TreeNode().treeOf(root))
        expected = 6
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [-10,9,20,None,None,15,7]
        actual = Solution().maxPathSum(TreeNode().treeOf(root))
        expected = 42
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = [-3]
        actual = Solution().maxPathSum(TreeNode().treeOf(root))
        expected = -3 
        self.assertEqual(actual, expected)

