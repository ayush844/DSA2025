class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        return self.winner(n, k)+1

    def winner(self, n, k):
        if n == 1:
            return 0
        return (self.winner(n-1, k)+k)%n