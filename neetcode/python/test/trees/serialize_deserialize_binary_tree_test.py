import unittest
from src.trees.treenode import TreeNode
from src.trees.serialize_deserialize_binary_tree import Codec

class SerializeDeserializeBinaryTreeTest(unittest.TestCase):
    def test_example1(self):
        root = [1,2,3,None,None,4,5]
        ser = Codec()
        deser = Codec()
        actual = (
            TreeNode().listOf(
                deser.deserialize(
                    ser.serialize(
                        TreeNode().treeOf(root)
                    )
                )
            )
        )
        # listOf() currently is just a level-order list, not including None values
        expected = TreeNode().listOf(TreeNode().treeOf([1,2,3,None,None,4,5]))
        self.assertEqual(actual, expected)

    def test_example2(self):
        root = []
        ser = Codec()
        deser = Codec()
        actual = (
            TreeNode().listOf(
                deser.deserialize(
                    ser.serialize(
                        TreeNode().treeOf(root)
                    )
                )
            )
        )
        expected = TreeNode().listOf(TreeNode().treeOf([]))
        self.assertEqual(actual, expected)

    def test_example3(self):
        root = [1,2,3,None,None,4,5,6,7]
        ser = Codec()
        deser = Codec()
        actual = (
            TreeNode().listOf(
                deser.deserialize(
                    ser.serialize(
                        TreeNode().treeOf(root)
                    )
                )
            )
        )
        expected = TreeNode().listOf(TreeNode().treeOf([1,2,3,None,None,4,5,6,7]))
        self.assertEqual(actual, expected)
