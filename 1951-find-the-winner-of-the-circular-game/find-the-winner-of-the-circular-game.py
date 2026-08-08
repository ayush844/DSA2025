class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]

        def helper(arr, start_index):
            if len(arr) == 1:
                return arr[0]

            index_to_delete = (start_index + k - 1) % len(arr)

            del arr[index_to_delete]

            return helper(arr, index_to_delete)
        
        return helper(arr, 0)