from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def naiveMaxPathSum(self, root: TreeNode) -> int:
        maxPathSum = float('-inf')
        st = [root]
        while st:
            curr = st.pop()
            maxPathSum = max(maxPathSum, self.pathSum(curr))
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)

        return maxPathSum

    def maxPathSum(self, root: TreeNode) -> int:
        currPath, maxPath = self.dfs(root)
        return maxPath

    # returns (current sum path, max sum path)
    def dfs(self, root: TreeNode) -> (int, int):
        if not root:
            return 0, float('-inf')

        # generate left and right path
        leftPath, maxLeftPath = self.dfs(root.left)
        rightPath, maxRightPath = self.dfs(root.right)

        # ignore paths that start at negative numbers
        leftPath = max(leftPath, 0)
        rightPath = max(rightPath, 0)

        # save max path
        currPath = leftPath + rightPath + root.val
        maxPath = max(maxLeftPath, maxRightPath, currPath)

        # return max of both paths, and pass max path
        return max(leftPath, rightPath) + root.val, maxPath 
'''
see: diameter of a graph
idea 1: sum all the paths for every node
    - guaranteed solution, but it's O(n^2)
idea 2: save previous paths
    - if we calculate the paths in a subtree, 
        the parent tree shouldn't have to recalulate the sum of the paths
        in the subtree; just add the parent node and other subtree path
    for this we should recursively get the path sums of the subtree paths

max(dfs, 0)
for every node, if a child is negative, then that path will
not generate a better solution -- i.e. starting a path from
a negative child is always worse than starting a path from a positive parent
'''
