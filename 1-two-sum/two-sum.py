class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ht = {}
        for i in range(n):
            needed = target - nums[i]
            if needed in ht:
                return [i, ht[needed]]
            ht[nums[i]] = i

        return []