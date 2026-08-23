class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
    
        dp = [[0]*n for _ in range(n)]

        max_res = [0, 0, 0]

        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if i == j:
                    dp[i][j] = True
                    if j-i+1 > max_res[0]:
                        max_res = [j-i+1, i, j]
                elif s[i] == s[j] and (j == i+1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > max_res[0]:
                        max_res = [j-i+1, i, j]
                else:
                    dp[i][j] = False
                    
        return s[max_res[1]:max_res[2]+1]
                    