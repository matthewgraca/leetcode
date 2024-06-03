import unittest
from src.trees.treenode import TreeNode
from src.trees.kth_smallest_in_bst import Solution

class KthSmallestInBSTTest(unittest.TestCase):
    def test_example1(self):
        root, k = TreeNode().treeOf([3,1,4,None,2]), 1
        actual = Solution().kthSmallest(root, k)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example2(self):
        root, k = TreeNode().treeOf([5,3,6,2,4,None,None,1]), 3
        actual = Solution().kthSmallest(root, k)
        expected = 3
        self.assertEqual(actual, expected)

    def test_example3(self):
        root, k = TreeNode().treeOf([3,1,4,None,2]), 3
        actual = Solution().kthSmallest(root, k)
        expected = 3
        self.assertEqual(actual, expected)
