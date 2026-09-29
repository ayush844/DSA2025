# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(node, min_value, max_value):
            if not node:
                return True

            if not (node.val > min_value and node.val < max_value):
                return False

            isLeftBST = helper(node.left, min_value, node.val)
            isRightBST = helper(node.right, node.val, max_value)

            return isLeftBST and isRightBST

        return helper(root, float('-inf'), float('inf'))