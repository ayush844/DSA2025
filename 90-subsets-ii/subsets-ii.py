class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        curr = []

        def helper(index):
            if index == n:
                res.append(curr[:])
                return
            
            curr.append(nums[index])
            helper(index+1)
            curr.pop()

            i = index
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            helper(i+1)



        helper(0)
        return res