from src.trees.treenode import TreeNode

class Solution:
    def __init__(self):
        pass

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        st = []
        curr, kth = root, root.val
        for _ in range(k):
            # in-order traversal gives smallest node in a bst
            while curr:
                st.append(curr)
                curr = curr.left

            kth = st[-1].val
            curr = st.pop()
            curr = curr.right
        return kth 
'''
The idea is to incrementally find the smallest node, one at a time.

the trick is that the leftmost node in a bst is the smallest node in the tree.

So to find the next smallest node, you go to the right tree and search for the 
leftmost node; i.e. in-order traversal

continue in this manner k times, and you get the kth smallest node in a bst.

as for the follow up, i think the answer is simply a min heap.


if k = n with n being the number of nodes in the tree, then the 
complexity is O(n).
'''
