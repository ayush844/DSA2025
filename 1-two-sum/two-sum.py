class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        n = len(nums)
        for i in range(n):
            req = target - nums[i]
            if req in hash:
                return [i, hash[req]]

            hash[nums[i]] = i

        return [-1, -1]