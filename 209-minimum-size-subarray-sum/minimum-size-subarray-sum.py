class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum = 0
        n = len(nums)
        length = float('inf')

        for right in range(n):
            curr_sum+=nums[right]

            while curr_sum >= target:
                new_length = right-left+1
                if new_length < length:
                    length = new_length

                curr_sum-=nums[left]
                left+=1

        return length if length != float('inf') else 0