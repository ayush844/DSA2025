class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        memo = {}
        
        def helper(i, j):

            if i == n or j == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + helper(i+1, j+1)
                return memo[(i, j)]

            memo[(i, j)] =  max(helper(i+1, j), helper(i, j+1))
            return memo[(i, j)]

        return helper(0, 0)