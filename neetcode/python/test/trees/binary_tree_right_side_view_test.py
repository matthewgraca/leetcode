import unittest
from src.trees.treenode import TreeNode
from src.trees.binary_tree_right_side_view import Solution

class BinaryTreeRightSideViewTest(unittest.TestCase):
    def test_example1(self):
        root = [1,2,3,None,5,None,4]
        actual = Solution().rightSideView(TreeNode().treeOf(root))
        expected = [1,3,4]
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [1,None,3]
        actual = Solution().rightSideView(TreeNode().treeOf(root))
        expected = [1,3]
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = []
        actual = Solution().rightSideView(TreeNode().treeOf(root))
        expected = []
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = [1,2]
        actual = Solution().rightSideView(TreeNode().treeOf(root))
        expected = [1,2]
        self.assertEqual(actual, expected)
