# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        n = len(inorder)
        idx = 0

        def helper(start, end):
            nonlocal idx

            if start > end:
                return None

            node_val = preorder[idx]
            node = TreeNode(node_val)

            idx+=1

            mid = inorder_idx[node_val]
            node.left = helper(start, mid-1)
            node.right = helper(mid+1, end)


            return node

        return helper(0, n-1)