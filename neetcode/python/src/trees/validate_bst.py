from src.trees.treenode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    def isValidBST(self, root: TreeNode) -> bool:
        return self.bfs(root)
        #return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node: TreeNode, leftVal: int, rightVal: int) -> bool:
        if not node:
            return True
        if node.val <= leftVal or node.val >= rightVal:
            return False

        return(
            self.dfs(node.left, leftVal, node.val) and
            self.dfs(node.right, node.val, rightVal)
        )

    def bfs(self, node: TreeNode) -> bool:
        if not node:
            return True

        q = deque()
        q.append((node, float('-inf'), float('inf')))
        while q:
            curr, minAncestor, maxAncestor = q.popleft()

            # check BST invariant: minAncestor < curr.val < maxAncestor
            if not (minAncestor < curr.val < maxAncestor):
                return False

            # ceiling of left tree is current value
            if curr.left:
                q.append((curr.left, minAncestor, curr.val))
            # floor of right tree is current value
            if curr.right:
                q.append((curr.right, curr.val, maxAncestor))
        return True
'''
seems like the same situtation as the previous problem about maintaining 
the heap invariant, this time with slightly different conditionals

So let me just copy that code and modify it

if you are a left node, all your parents are larger
if you are a right node, all your parents are smaller

tracking strictly the parent isn't enough. the input may be valid for each node,
but not in terms of the rest of the tree; so we need to track max/min
    - for each left node, it should be smaller than all its ancestors
    - for each right node, it should be larger than all its ancestors


Ok the biggest problem is that when we go to the left or right tree, our max/min 
ancestor trick fails because the conditional is entirely based on whether we're
in a left or right tree. if we're in a right tree vs left tree, our conditionals 
end up flipping.

Instead, the trick here is that by using dfs, we can go to the left/right tree and 
pass in different parameters based on that.

For the left tree, we change the ceiling value, and for the right tree we change the 
floor value.

So the idea here is: for each node, the node needs to be within a range to be a BST.
When we go to the left tree, values should be smaller, so the ceiling needs to come down,
but the floor shouldn't update (based on ancestor nodes)
For the right tree, values should be larger, so the floor needs to come up, but the 
ceiling shouldn't update (based on ancestor nodes)

The great thing about dfs is that we know when we're going left and going right, so we 
can update the floor and ceiling based on whether we go left or right.


The only major diff b/t bfs and dfs is that the dfs is recursive, so our bfs 
solution fails fast instead of checking every single node.
'''
