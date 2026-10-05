class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        results = []

        def dfs(num, digit_left):
            if digit_left == 0:
                results.append(num)
                return

            last = num % 10

            if last + k <= 9:
                dfs(num*10 + last + k, digit_left-1)

            if last - k >= 0 and k!=0:
                dfs(num*10 + last - k, digit_left-1)

        for first_digit in range(1, 10):
            dfs(first_digit, n-1)

        return results