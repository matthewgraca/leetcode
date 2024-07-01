from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        st = []
        curr, kth = root, root.val
        
        # in-order traversal gives smallest node in a bst
        for _ in range(k):
            # go leftmost
            while curr:
                st.append(curr)
                curr = curr.left

            # inorder
            kth = st[-1].val

            # go right 1
            curr = st.pop()
            curr = curr.right

        return kth 

    # putting the abstract version of iterative inorder traversal
    def inorder(self, root, k: int) -> int:
        if not root:
            return -1

        st = []
        curr, kth = root, root.val
        while st:
            # go leftmost
            while curr:
                st.append(curr)
                curr = curr.left

            # inorderr
            k -= 1
            if k == 0:
                kth = st[-1].val

            # go right 1
            curr = st.pop()
            curr = curr.right

        return kth
