# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque([root])
        result = []
        if not root:
            return result

        l2r = True
        while queue:
            length = len(queue)
            level = []
            count = 0

            while count < length:
                node = queue.popleft()
                count+=1
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if not l2r:
                result.append(level[::-1])
            else:
                result.append(level)

            l2r = not l2r


        return result