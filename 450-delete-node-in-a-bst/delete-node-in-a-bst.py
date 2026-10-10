# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        tree = root

        if tree.val > key:
            tree.left = self.deleteNode(tree.left, key)
        elif tree.val < key:
            tree.right = self.deleteNode(tree.right, key)
        else:
            if not tree.left:
                return tree.right
            if not tree.right:
                return tree.left
        
            next = tree.right
            while next.left:
                next = next.left

            tree.val = next.val
            tree.right = self.deleteNode(tree.right, next.val)

        return root