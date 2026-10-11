# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(node, min, max):
            if not node:
                return True

            if not (node.val > min and node.val < max):
                return False

            isLeftBST = helper(node.left, min, node.val)
            isRightBST = helper(node.right, node.val, max)

            return isLeftBST and isRightBST

        return helper(root, float('-inf'), float('inf'))