import unittest
from src.trees.treenode import TreeNode
from src.trees.subtree_of_another_tree import Solution

class SubtreeOfAnotherTreeTest(unittest.TestCase):
    def test_example1(self):
        root, subroot = [3,4,5,1,2], [4,1,2]
        actual =    Solution().isSubtree(
                        TreeNode().treeOf(root), TreeNode().treeOf(subroot)
                    )
        expected = True
        self.assertEqual(actual, expected)


    def test_example2(self):
        root, subroot = [3,4,5,1,2,None,None,None,None,0], [4,1,2]
        actual =    Solution().isSubtree(
                        TreeNode().treeOf(root), TreeNode().treeOf(subroot)
                    )
        expected = False 
        self.assertEqual(actual, expected)

    def test_example3(self):
        root, subroot = [1], [0]
        actual =    Solution().isSubtree(
                        TreeNode().treeOf(root), TreeNode().treeOf(subroot)
                    )
        expected = False 
        self.assertEqual(actual, expected)

    def test_example4(self):
        root, subroot = [1,1], [1]
        actual =    Solution().isSubtree(
                        TreeNode().treeOf(root), TreeNode().treeOf(subroot)
                    )
        expected = True 
        self.assertEqual(actual, expected)
