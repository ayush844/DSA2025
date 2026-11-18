class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, _ = stack.pop()
                res[j] = i-j

            stack.append((i, temp))


        return res