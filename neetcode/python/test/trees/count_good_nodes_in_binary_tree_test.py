import unittest
from src.trees.treenode import TreeNode
from src.trees.count_good_nodes_in_binary_tree import Solution

class CountGoodNodesInBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = [3,1,4,3,None,1,5]
        actual = Solution().goodNodes(TreeNode().treeOf(root))
        expected = 4
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = [3,3,None,4,2]
        actual = Solution().goodNodes(TreeNode().treeOf(root))
        expected = 3
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = [1]
        actual = Solution().goodNodes(TreeNode().treeOf(root))
        expected = 1
        self.assertEqual(actual, expected)

    def test_example4(self):
        root = [9,None,3,6]
        actual = Solution().goodNodes(TreeNode().treeOf(root))
        expected = 1
        self.assertEqual(actual, expected)

    def test_example5(self):
        root = [
            -1,5,-2,4,4,2,-2,None,None,
            -4,None,-2,3,None,-2,0,None,
            -1,None,-3,None,-4,-3,3,None,
            None,None,None,None,None,None,3,-3
        ]
        actual = Solution().goodNodes(TreeNode().treeOf(root))
        expected = 5
        self.assertEqual(actual, expected)
