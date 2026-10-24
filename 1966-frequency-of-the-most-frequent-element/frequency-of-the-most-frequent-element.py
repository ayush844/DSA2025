class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        max_frequency = 1
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum+=nums[right]

            while nums[right]*(right-left+1) > curr_sum+k:
                curr_sum-=nums[left]
                left+=1

            max_frequency = max(max_frequency, right-left+1)

        return max_frequency