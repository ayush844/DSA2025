class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = max_prod = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            curr_max, curr_min = (
                max(x, curr_max * x, curr_min * x),
                min(x, curr_max * x, curr_min * x)
            )

            max_prod = max(max_prod, curr_max)

        return max_prod