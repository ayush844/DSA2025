class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(index):
            if index == n-1:
                res.append(nums[:])
                return
            hash = {}
            for j in range(index, n):
                if nums[j] not in hash:
                    hash[nums[j]] = True
                    nums[index], nums[j] = nums[j], nums[index]
                    helper(index + 1)
                    nums[index], nums[j] = nums[j], nums[index]

        helper(0)

        return res
        
        