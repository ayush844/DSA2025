class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        output = []

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

        output.append(nums[q[0]])

        n = len(nums)

        for i in range(k, n):
            if q[0] == i-k:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)
            output.append(nums[q[0]])

        return output