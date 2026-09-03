class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def helper(index):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(index, n+1):
                curr.append(i)
                helper(i+1)
                curr.pop()

        helper(1)
        return res