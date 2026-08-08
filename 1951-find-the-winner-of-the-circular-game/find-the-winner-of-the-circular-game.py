class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def josephus(n):
            if n==1:
                return 0

            return (josephus(n-1) + k) % n

        return josephus(n) + 1
        