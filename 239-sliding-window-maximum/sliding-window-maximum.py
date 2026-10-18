class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        dq = deque()
        output = []

        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        output.append(nums[dq[0]])

        for i in range(k, n):
            if dq[0] == i-k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            output.append(nums[dq[0]])

        return output