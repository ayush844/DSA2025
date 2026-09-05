class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[-1]*(m) for _ in range(n)]

        def helper(i, j):
            if i >=n and j >= m:
                return 0
            if i >= n:
                return m-j
            if j >= m:
                return n-i

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = helper(i+1, j+1)
            else:
                insert = 1+helper(i, j+1)
                delete = 1+helper(i+1, j)
                replace = 1+helper(i+1, j+1)
                dp[i][j] = min(insert, delete, replace)

            return dp[i][j]

        return helper(0, 0)