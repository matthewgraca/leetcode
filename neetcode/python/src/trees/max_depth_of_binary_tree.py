from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 

        st = [(root,1)]
        maxDepth = 0
        while st:
            node, depth = st.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                st.append((node.left, depth+1))
            if node.right:
                st.append((node.right, depth+1))

        return maxDepth 


    def maxDepthR(self, root: TreeNode) -> int:
        if root is None:
            return 0

        leftTreeDepth = 1 + self.maxDepthR(root.left)
        rightTreeDepth = 1 + self.maxDepthR(root.right)

        return max(leftTreeDepth, rightTreeDepth)

'''
Easy to think of this as a mathematical object...
in fact, anything that you pass in that doesn't have state can be thought kinda like this, no?
T(n) = 1 + T(n-1) + 1 + T(n-1) = 2 + 2T(n-1)

Time:
    O(n); traverse n nodes
Space:
    O(n), for degenerate binary trees
'''
