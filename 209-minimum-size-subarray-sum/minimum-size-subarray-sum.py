class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        length = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                new_len = right - left + 1
                if new_len < length:
                    length = new_len
                curr_sum-=nums[left]
                left += 1

        return length if length != float("inf") else 0