import unittest
from src.trees.treenode import TreeNode
from src.trees.validate_bst import Solution

class ValidateBSTTest(unittest.TestCase):
    def test_example1(self):
        root = [2,1,3]
        actual = Solution().isValidBST(TreeNode().treeOf(root))
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [5,1,4,None,None,3,6]
        actual = Solution().isValidBST(TreeNode().treeOf(root))
        expected = False 
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = [2,2,2]
        actual = Solution().isValidBST(TreeNode().treeOf(root))
        expected = False 
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = [5,4,6,None,None,3,7]
        actual = Solution().isValidBST(TreeNode().treeOf(root))
        expected = False 
        self.assertEqual(actual, expected)
