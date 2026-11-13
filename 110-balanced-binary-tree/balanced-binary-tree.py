# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        left_ht = self.getHeight(root.left)
        right_ht = self.getHeight(root.right)

        if abs(left_ht - right_ht) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node):
        if not node:
            return 0

        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        return max(left, right) + 1