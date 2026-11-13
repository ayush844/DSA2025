# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return -1

        inorder_arr = self.inorder(root)

        return inorder_arr[k-1]

    def inorder(self, root):
        res = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)

        return res