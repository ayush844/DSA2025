class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        max_len = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1

            max_len = max(max_len, dp[i])

        return max_len