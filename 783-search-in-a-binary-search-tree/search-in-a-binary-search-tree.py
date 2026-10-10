# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None

        tree = root
        while tree:
            if tree.val == val:
                return tree
            elif tree.val < val:
                tree = tree.right
            else:
                tree = tree.left

        return None