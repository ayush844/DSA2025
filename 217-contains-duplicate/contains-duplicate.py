class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        ht = {}

        for i in range(n):
            if nums[i] in ht:
                return True
            ht[nums[i]] = i

        return False