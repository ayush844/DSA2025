class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum = 0
        length = float('inf')
        n = len(nums)

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                new_len = right - left + 1
                if new_len < length:
                    length = new_len

                curr_sum-=nums[left]
                left+=1

        return length if length != float('inf') else 0