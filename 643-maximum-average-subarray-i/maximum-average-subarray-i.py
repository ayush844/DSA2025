class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = 0

        for i in range(k):
            curr_sum+=nums[i]

        max_sum = curr_sum

        n = len(nums)

        for i in range(k, n):
            curr_sum = curr_sum+nums[i]-nums[i-k]

            max_sum = max(max_sum, curr_sum)

        return max_sum/k