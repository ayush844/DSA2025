# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = TreeNode(val)

        if not root:
            return node

        tree = root
        while True:
            if val > tree.val:
                if not tree.right:
                    tree.right = node
                    return root
                tree = tree.right
            else:
                if not tree.left:
                    tree.left = node
                    return root
                tree = tree.left