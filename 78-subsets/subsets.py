class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []

        def helper(index):
            if index == n:
                res.append(curr[:])
                return
            
            helper(index+1)
            curr.append(nums[index])
            helper(index+1)
            curr.pop()

        helper(0)

        return res