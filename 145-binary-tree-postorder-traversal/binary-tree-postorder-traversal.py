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
        array = []
        current = root

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            array.append(node.val)
        
        traverse(current)

        return array