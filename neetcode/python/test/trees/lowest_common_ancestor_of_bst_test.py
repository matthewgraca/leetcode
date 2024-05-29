import unittest
from src.trees.treenode import TreeNode
from src.trees.lowest_common_ancestor_of_bst import Solution

class LowestCommonAncestorOfBstTest(unittest.TestCase):
    def test_example1(self):
        root, p, q = [6,2,8,0,4,7,9,None,None,3,5], 2, 8
        # convert input to TreeNodes, convert output to list, take the first int
        actual =    TreeNode().listOf(
                        Solution().lowestCommonAncestor(
                            TreeNode().treeOf(root), 
                            TreeNode().treeOf(p), 
                            TreeNode().treeOf(q)
                        )
                    )[0]
        expected = 6
        self.assertEqual(actual, expected)

    def test_example2(self):
        root, p, q = [6,2,8,0,4,7,9,None,None,3,5], 2, 4
        # convert input to TreeNodes, convert output to list, take the first int
        actual =    TreeNode().listOf(
                        Solution().lowestCommonAncestor(
                            TreeNode().treeOf(root), 
                            TreeNode().treeOf(p), 
                            TreeNode().treeOf(q)
                        )
                    )[0]
        expected = 2
        self.assertEqual(actual, expected)

    def test_example3(self):
        root, p, q = [2,1], 2, 1
        # convert input to TreeNodes, convert output to list, take the first int
        actual =    TreeNode().listOf(
                        Solution().lowestCommonAncestor(
                            TreeNode().treeOf(root), 
                            TreeNode().treeOf(p), 
                            TreeNode().treeOf(q)
                        )
                    )[0]
        expected = 2
        self.assertEqual(actual, expected)

    def test_example4(self):
        root, p, q = [3,1,4,None,2], 2, 4
        # convert input to TreeNodes, convert output to list, take the first int
        actual =    TreeNode().listOf(
                        Solution().lowestCommonAncestor(
                            TreeNode().treeOf(root), 
                            TreeNode().treeOf(p), 
                            TreeNode().treeOf(q)
                        )
                    )[0]
        expected = 3
        self.assertEqual(actual, expected)
