import unittest
from src.trees.treenode import TreeNode
from src.trees.balanced_binary_tree import Solution

class BalancedBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = [3,9,20,None,None,15,7]
        actual = Solution().isBalanced(TreeNode().treeOf(root))
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [1,2,2,3,3,None,None,4,4]
        actual = Solution().isBalanced(TreeNode().treeOf(root))
        expected = False 
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = []
        actual = Solution().isBalanced(TreeNode().treeOf(root))
        expected = True 
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = [1,2,2,3,None,None,3,4,None,None,4]
        actual = Solution().isBalanced(TreeNode().treeOf(root))
        expected = False 
        self.assertEqual(actual, expected)
