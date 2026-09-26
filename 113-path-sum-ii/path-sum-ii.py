# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        path = []
        res = []

        def dfs(node):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                res.append(path[:])
            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)
        ans = []
        for i in res:
            if sum(i) == targetSum:
                ans.append(i)

        return ans