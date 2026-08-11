class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def helper(index, target):
            if target == 0:
                res.append(sub[:])
                return
            if target < 0:
                return

            for i in range(index, len(candidates)):
                if(i > index and candidates[i] == candidates[i-1]):
                    continue
                sub.append(candidates[i])
                helper(i + 1, target - candidates[i])

                sub.pop()
        
        helper(0, target)

        return res