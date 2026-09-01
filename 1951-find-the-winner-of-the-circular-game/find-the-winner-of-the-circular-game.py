class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]

        return self.winner(arr, 0, k)

    def winner(self, arr, start, k):
        if len(arr) == 1:
            return arr[0]
        index_to_remove = (start + k - 1)%len(arr)

        del arr[index_to_remove]

        return self.winner(arr, index_to_remove%len(arr), k)