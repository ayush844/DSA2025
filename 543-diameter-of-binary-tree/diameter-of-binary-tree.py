# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(node):
            nonlocal max_diam
            if not node:
                return -1

            left_ht = dfs(node.left)
            right_ht = dfs(node.right)

            diameter = left_ht + right_ht + 2
            max_diam = max(max_diam, diameter)

            return max(left_ht, right_ht)+1

        dfs(root)

        return max_diam