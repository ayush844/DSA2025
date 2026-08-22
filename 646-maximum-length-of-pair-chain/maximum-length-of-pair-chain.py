class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1]*n

        longest_chain = 1

        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and (dp[j]+1) > dp[i]:
                    dp[i] = dp[j]+1

            if longest_chain < dp[i]:
                longest_chain = dp[i]
        
        return longest_chain