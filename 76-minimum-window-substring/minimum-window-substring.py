class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        sliding_window = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        need = len(count_t)
        left = 0
        have = 0
        n = len(s)
        res = [-1, -1]
        res_len = float('inf')

        for right in range(n):
            c = s[right]
            sliding_window[c] = sliding_window.get(c, 0) + 1

            if c in count_t and count_t[c] == sliding_window[c]:
                have+=1

            while have == need:
                if right - left+1 < res_len:
                    res = [left, right]
                    res_len = right-left+1

                sliding_window[s[left]] -= 1
                if s[left] in count_t and sliding_window[s[left]] < count_t[s[left]]:
                    have-=1

                left+=1

        left, right = res

        return s[left: right+1] if res_len != float('inf') else ""