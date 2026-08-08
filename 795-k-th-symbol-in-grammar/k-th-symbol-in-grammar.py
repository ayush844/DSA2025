class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        size = 2 ** (n-1)
        mid = size // 2
        if k > mid:
            return 1 - self.kthGrammar(n-1, k-mid)
        else:
            return self.kthGrammar(n-1, k)