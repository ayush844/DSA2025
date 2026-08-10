class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def helper(index):
            if index == len(nums):
                res.append(subset[:])
                return
            # exclude
            helper(index+1)

            # include
            subset.append(nums[index])
            helper(index + 1)

            # backtrack our changes
            subset.pop()


        helper(0)
        return res