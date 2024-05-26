import unittest
from src.trees.treenode import TreeNode

class TreeNodeTest(unittest.TestCase):
    def test_example1(self):
        root = [1,2,3,4,5,6,7]
        actual = TreeNode().treeOf(root)
        # dfs
        # left tree
        self.assertEqual(actual.val, 1)
        self.assertEqual(actual.left.val, 2)
        self.assertEqual(actual.left.left.val, 4)
        self.assertTrue(actual.left.left.left is None)
        self.assertTrue(actual.left.left.right is None)
        self.assertEqual(actual.left.right.val, 5)
        self.assertTrue(actual.left.right.left is None) 
        self.assertTrue(actual.left.right.right is None) 

        # right tree
        self.assertEqual(actual.right.val, 3)
        self.assertEqual(actual.right.left.val, 6)
        self.assertTrue(actual.right.left.left is None)
        self.assertTrue(actual.right.left.right is None)
        self.assertEqual(actual.right.right.val, 7)
        self.assertTrue(actual.right.right.left is None)
        self.assertTrue(actual.right.right.right is None)

    def test_example2(self):
        root = [1,2,3,4,5,6,7]
        nodeifiedRoot = TreeNode().treeOf(root)
        listifiedRoot = TreeNode().listOf(nodeifiedRoot)
        self.assertEqual(root, listifiedRoot)
        
