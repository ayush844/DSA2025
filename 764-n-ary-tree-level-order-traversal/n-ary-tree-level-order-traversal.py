"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque([root])

        if not root:
            return []

        res = []

        while queue:
            length = len(queue)
            count = 0
            level = []

            while count < length:
                node = queue.popleft()
                level.append(node.val)
                count+=1

                for child in node.children:
                    queue.append(child)

            res.append(level)


        return res