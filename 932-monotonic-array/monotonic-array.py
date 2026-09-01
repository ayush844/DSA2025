class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if nums[0] > nums[n-1]:
            for i in range(n-1):
                if nums[i] < nums[i+1]:
                    return False
        elif nums[0] == nums[n-1]:
            for i in range(n-1):
                if nums[i] != nums[i+1]:
                    return False
        else:
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return False

        return True