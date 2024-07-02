from src.trees.treenode import TreeNode
from collections import deque

class Codec:
    def __init_(self):
        pass

    def serialize(self, root: TreeNode) -> str:
        # None implies no subtrees from root; denote with "N"
        if not root:
            return "N"

        # preorder dfs
        val = str(root.val)
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return f"{val},{left},{right}" 

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        # convert string to queue, then deserialize
        dataList = deque(data.split(","))
        return self.deserializeList(dataList)

    def deserializeList(self, data: deque)-> TreeNode:
        # base case: empty list = no subtrees
        if not data:
            return None

        # case 1: N implies no subtrees
        val = data.popleft()
        if val == "N":
            return None

        # case 2: valid node; use preorder dfs
        node = TreeNode(int(val))
        node.left = self.deserializeList(data)
        node.right = self.deserializeList(data)

        return node
