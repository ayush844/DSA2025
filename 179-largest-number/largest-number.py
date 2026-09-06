class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=cmp_to_key(lambda a, b: -1 if a+b>b+a else 1))

        if nums[0]=='0':
            return "0"

        else:
            return "".join(nums)