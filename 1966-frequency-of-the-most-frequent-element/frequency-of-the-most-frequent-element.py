class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        n = len(nums)
        total = 0
        res = 0

        for right in range(n):
            total += nums[right]

            while nums[right]*(right-left+1) > total+k:
                total -= nums[left]
                left+=1

            res = max(res, right-left+1)

        return res