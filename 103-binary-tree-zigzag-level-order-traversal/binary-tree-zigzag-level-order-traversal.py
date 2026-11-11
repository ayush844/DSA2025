# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        l2r = True
        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            length = len(queue)
            count = 0
            level = []

            while count < length:
                node = queue.popleft()
                level.append(node.val)
                count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if l2r:
                res.append(level)
            else:
                res.append(level[::-1])

            l2r = not l2r

        return res