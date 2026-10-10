# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        output = []
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            traverse(node.right)
            
            output.append(node.val)

        traverse(root)

        return output