from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init__(self):
        pass

    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res 

        # level-order traversal, but nodes are saved from right -> left
        q = [root]
        while q:
            currLevel = []
            while q:
                currLevel.append(q.pop(0))

            res.append(currLevel[0].val) # rightmost value on the current level 
            while currLevel:
                node = currLevel.pop(0)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return res
'''
Seems like dfs but you're going to the right instead of classically, the left
Straight up ignore all the left nodes? we'll see with tests.

OK this is a bit freaky; it's more like taking the binary tree and rotating 
it so that it lays on the left side. So if there are ONLY left nodes and no 
right nodes, you'll still "see" the left nodes.

this seems more like bfs; if there is a right node, add that to the list;
if there is no right node and there is a left node, add that to the list.

so we start off with classic bfs and attempt to add this extra conditional 
that allows us to track right nodes; BUT track left nodes if there is no right node
in the way.

More specifically, this seems more like level-order traversal but keeping the 
rightmost node value.

time:
    O(n) to traverse n nodes for order-level traversal
space:
    O(1) for only constant space used, not including output space
'''
