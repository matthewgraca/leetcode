import unittest
from src.trees.treenode import TreeNode
from src.trees.binary_tree_level_order_traversal import Solution

class BinaryTreeLevelOrderTraversalTest(unittest.TestCase):
    def test_example1(self):
        root = [3,9,20,None,None,15,7]
        actual = Solution().levelOrder(TreeNode().treeOf(root))
        expected = [[3],[9,20],[15,7]]
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [1]
        actual = Solution().levelOrder(TreeNode().treeOf(root))
        expected = [[1]]
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = []
        actual = Solution().levelOrder(TreeNode().treeOf(root))
        expected = []
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = [1,2,3,4,None,None,5]
        actual = Solution().levelOrder(TreeNode().treeOf(root))
        expected = [[1],[2,3],[4,5]]
        self.assertEqual(actual, expected)
