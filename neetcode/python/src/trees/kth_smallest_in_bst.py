from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return float('-inf')
        
        # in-order traversal gives smallest node in a bst
        st = [root]
        curr, kth = root, root.val
        while st and k > 0:
            # go leftmost
            while curr:
                st.append(curr)
                curr = curr.left

            # inorder
            k -= 1
            kth = st[-1].val

            # go right 1
            curr = st.pop()
            curr = curr.right

        return kth 
