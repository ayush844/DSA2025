class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        res = []
        curr = []

        def helper(index, remaining):
            if remaining < 0 or index >= n:
                return
            if remaining == 0:
                res.append(curr[:])
                return

            for i in range(index, n):
                curr.append(candidates[i])
                helper(i, remaining-candidates[i])
                curr.pop()

        helper(0, target)
        return res