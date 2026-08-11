class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        sub = []

        def helper(index, remaining):
            if remaining == 0:
                res.append(sub[:])
                return
            if remaining < 0:
                return
            
            for i in range(index, len(candidates)):
                sub.append(candidates[i])
                helper(i, remaining - candidates[i])
                sub.pop()
        
        helper(0, target)

        return res
        