class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        low = 0
        high = n-1

        first, last = -1, -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        low = 0
        high = n-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        return [first, last]