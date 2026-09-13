class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        max_len = 1
        n = len(pairs)
        dp = [1]*n

        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1

            max_len = max(max_len, dp[i])

        return max_len