class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr_win_sum = 0
        res = 0
        for right in range(len(nums)):
            curr_win_sum += nums[right]

            while nums[right]*(right - left + 1) > (curr_win_sum + k):
                curr_win_sum -= nums[left]
                left += 1

            res = max(res, right-left+1)

        return res