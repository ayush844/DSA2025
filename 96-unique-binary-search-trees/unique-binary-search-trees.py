class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]

        dp[0] = 1
        dp[1] = 1

        for total in range(2, n+1):
            for root in range(total):
                left = root
                right = total - root - 1
                dp[total] += dp[left]*dp[right]

        return dp[n]