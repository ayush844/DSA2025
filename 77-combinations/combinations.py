class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i+1 for i in range(n)]
        res = []
        sub = []

        def helper(index):
            if len(sub) == k:
                res.append(sub[:])
                return
            
            for i in range(index, n):
                sub.append(arr[i])
                helper(i+1)
                sub.pop()

        helper(0)
        return res
        