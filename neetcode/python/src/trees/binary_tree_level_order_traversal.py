from src.trees.treenode import TreeNode
from typing import List

class Solution:
    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q, res = [root], []
        while q:
            # pop all nodes from q to the current level list, emptying q
            level = []
            while q:
                level.append(q.pop(0))

            # using the current level list, put all the nodes of the next level into q
            # now q will contain all the nodes in the next level only
            temp = []
            while level:
                curr = level.pop(0)
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)

        return res
'''
I like this solution more than neetcodes; it's the same but I kind of see the solution better

Time:
    - n nodes traversed
    - push a total of n nodes through the queue and the level list
    - Total: O(n)

Space:
    - queue and list have, at most, only the the current level's nodes contained.
        given the binary tree, only 2 nodes in the list at a time
        - so no matter how large the binary tree is, the queue and the level list doesn't change
    - O(1) for only constant space used. not including the output space
'''
