import unittest
from src.trees.treenode import TreeNode
from src.trees.same_tree import Solution

class SameTreeTest(unittest.TestCase):
    def test_example1(self):
        p, q = [1,2,3], [1,2,3]
        actual = Solution().isSameTree(
                        TreeNode().treeOf(p), TreeNode().treeOf(q)
                    )
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        p, q = [1,2], [1,None,2]
        actual = Solution().isSameTree(
                        TreeNode().treeOf(p), TreeNode().treeOf(q)
                    )
        expected = False 
        self.assertEqual(actual, expected)

    def test_example3(self):
        p, q = [1,2,1], [1,1,2]
        actual = Solution().isSameTree(
                        TreeNode().treeOf(p), TreeNode().treeOf(q)
                    )
        expected = False 
        self.assertEqual(actual, expected)

    def test_example4(self):
        p, q = [3,2,1], [1,2,3]
        actual = Solution().isSameTree(
                        TreeNode().treeOf(p), TreeNode().treeOf(q)
                    )
        expected = False 
        self.assertEqual(actual, expected)
