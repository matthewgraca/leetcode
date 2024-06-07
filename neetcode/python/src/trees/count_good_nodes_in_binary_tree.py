from src.trees.treenode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    # depth first search that also remembers the largest ancestor's value
    def dfs(self, root: TreeNode, maxVal: int) -> int:
        if not root:
            return 0

        # if the node is >= the max value of its ancestors, increment count
        count = 1 if root.val >= maxVal else 0

        maxVal = max(maxVal, root.val) 
        count += self.dfs(root.left, maxVal)
        count += self.dfs(root.right, maxVal)

        return count

    def bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        maxVal = root.val
        q = deque()
        q.append((root, maxVal))
        while q:
            currNode, maxVal = q.popleft()
            # if the node is larger than the largest value of its ancestors, 
            # then it is a good node
            if currNode.val >= maxVal:
                count += 1
                maxVal = currNode.val

            # bundle the children with the largest value of its direct ancestors
            if currNode.left:
                q.append((currNode.left, maxVal))
            if currNode.right:
                q.append((currNode.right, maxVal))

        return count

'''
This seems like this is a test of whether or not a binary tree is actually a 
min heap; that for every node, the keys of its children are smaller.

To do this, we check every node:
    - for each larger child, we increment "goodCount"
    - go to next node
as for traversal, let's try bfs for this

ok, node A is bad and B is a child of A, we need to check B against A's parent too


Plan B:
    we use dfs while passing in the max value for that tree
    when we get to the bottom of the tree, we will have the max value contained in this 
    tree at that point.
        specifically, at each function call, we have the max value AT THAT POINT, 
        ignoring the children. As we move to the next child, we update the max so we can 
        now make sure that child is properly not smaller than the nodes above it!!

So the trick here is "remembering the largest value of the ancestors" at each node
    -if the node is larger than or equal to the largest ancestor, the invariant is preserved
    -else it's over

same time and space as normal dfs
'''
