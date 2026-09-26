# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        array = []
        current = root

        def traverse(node):
            if node.left:
                traverse(node.left)
            array.append(node.val)
            if node.right:
                traverse(node.right)
        
        traverse(current)

        return array