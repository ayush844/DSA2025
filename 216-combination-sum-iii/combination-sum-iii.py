class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sub = []
        res = []
        arr = [i+1 for i in range(9)]

        def helper(index, target):
            if len(sub) == k and target == 0:
                res.append(sub[:])
                return
            if len(sub) >= k:
                return

            for i in range(index, len(arr)):
                sub.append(arr[i])
                helper(i+1, target - arr[i])
                sub.pop()

        helper(0, n)

        return res