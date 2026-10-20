class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0)+1

        need = len(count_t)
        have = 0

        left = 0
        n = len(s)
        res = [-1, -1]
        res_len = float('inf')
        sliding_window = {}

        for right in range(n):
            c = s[right]
            sliding_window[c] = sliding_window.get(c, 0)+1
            
            if c in count_t and count_t[c] == sliding_window[c]:
                have+=1

            while have == need:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right-left+1

                sliding_window[s[left]] -= 1
                if s[left] in count_t and count_t[s[left]] > sliding_window[s[left]]:
                    have-=1
                left+=1

        left, right = res
        return s[left: right+1] if res_len != float('inf') else ""