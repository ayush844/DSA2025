class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1]*(n+1) for i in range(n+1)]

        def helper(prev, curr):

            if curr == n:
                return 0

            if dp[curr][prev] != -1:
                return dp[curr][prev]

            exclude = helper(prev, curr+1)

            include = 0

            if nums[curr] > nums[prev] or prev == -1:
                include = 1 + helper(curr, curr+1)

            dp[curr][prev] = max(exclude, include)

            return dp[curr][prev]

        return helper(-1, 0)