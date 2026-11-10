# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []

        res = []

        def dfs(node, curr, rem_sum):
            if not node:
                return
            
            curr.append(node.val)
            rem_sum -= node.val
            if rem_sum == 0 and not node.left and not node.right:
                res.append(curr[:])

            dfs(node.left, curr, rem_sum)
            dfs(node.right, curr, rem_sum)

            curr.pop()

        dfs(root, [], targetSum)

        return res