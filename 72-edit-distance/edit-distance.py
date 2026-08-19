class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = {}

        def helper(i, j):
            if i == n:
                return m-j
            if j == m:
                return n-i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i+1, j+1)
                return memo[(i, j)]

            insert = helper(i, j+1)
            delete = helper(i+1, j)
            replace = helper(i+1, j+1)

            memo[(i, j)] = 1+min(insert, delete, replace)
            return memo[(i, j)]

        return helper(0, 0)
        