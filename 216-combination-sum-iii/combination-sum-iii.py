class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        curr = []
        res = []
        arr = [i+1 for i in range(9)]

        def helper(index, remaining):
            if len(curr) == k and remaining == 0:
                res.append(curr[:])
                return

            if index>=9 or remaining < 0:
                return

            for i in range(index, len(arr)):
                curr.append(arr[i])
                helper(i+1, remaining-arr[i])
                curr.pop()

        helper(0, n)

        return res