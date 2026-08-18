class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(target, num-1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[target]