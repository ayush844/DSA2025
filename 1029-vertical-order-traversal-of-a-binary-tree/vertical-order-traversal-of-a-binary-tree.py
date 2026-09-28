# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return None

        queue = deque([(root, 0, 0)])

        column = {}

        while queue:
            node, row, col = queue.popleft()

            if col not in column:
                column[col] = []

            column[col].append((row, node.val))

            if node.left: queue.append((node.left, row+1, col-1))
            if node.right: queue.append((node.right, row+1, col+1))

        output = []

        for col in sorted(column):
            column[col].sort()
            values = []
            for row, val in column[col]:
                values.append(val)
            
            output.append(values)

        return output