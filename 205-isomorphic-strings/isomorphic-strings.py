class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        ht_s = {}
        ht_t = {}

        for i in range(n):
            if s[i] not in ht_s:
                ht_s[s[i]] = t[i]
            if t[i] not in ht_t:
                ht_t[t[i]] = s[i]
            if ht_s[s[i]] != t[i] or ht_t[t[i]] != s[i]:
                return False

        return True