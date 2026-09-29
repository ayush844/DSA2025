# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def generate(start, end):
            if start > end:
                return [None]

            trees = []

            for root in range(start, end+1):
                left_tree = generate(start, root-1)
                right_tree = generate(root+1, end)

                for left in left_tree:
                    for right in right_tree:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return generate(1, n)