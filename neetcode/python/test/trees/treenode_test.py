import unittest
from src.trees.treenode import TreeNode

class TreeNodeTest(unittest.TestCase):
    def test_constructTreeNodeFromList(self):
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

    def test_convertListToTreeNodeAndBackToList(self):
        root = [1,2,3,4,5,6,7]
        nodeifiedRoot = TreeNode().treeOf(root)
        listifiedRoot = TreeNode().listOf(nodeifiedRoot)
        self.assertEqual(root, listifiedRoot)
        
    def test_constructIncompleteBinaryTreeFromList(self):
        nodeList = [3,9,20,None,None,15,7]
        node = TreeNode().treeOf(nodeList)

        # depth 0
        self.assertEqual(node.val, 3)
        # depth 1
        self.assertEqual(node.left.val, 9)
        self.assertEqual(node.right.val, 20)
        # depth 2
        self.assertTrue(node.left.left is None)
        self.assertTrue(node.left.right is None)
        self.assertEqual(node.right.left.val, 15)
        self.assertEqual(node.right.right.val, 7)
        # depth 3
        self.assertTrue(node.right.left.left is None)
        self.assertTrue(node.right.left.right is None)
        self.assertTrue(node.right.right.left is None)
        self.assertTrue(node.right.right.right is None)

    def test_intAsNode(self):
        node = 1
        root = TreeNode().treeOf(node)
        self.assertEqual(root.val, 1)
        self.assertTrue(root.left is None)
        self.assertTrue(root.right is None)
