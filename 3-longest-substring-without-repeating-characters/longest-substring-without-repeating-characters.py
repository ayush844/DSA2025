class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash = {}
        n = len(s)
        max_len = 0
        for right in range(n):
            if s[right] in hash:
                left = max(left, hash[s[right]]+1)
            
            hash[s[right]] = right

            max_len = max(max_len, right-left+1)

        return max_len