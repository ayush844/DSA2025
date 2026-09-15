class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n-1

        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if (target >= nums[left] and target <= nums[middle]):
                    right = middle-1
                else:
                    left = middle+1
            else:
                if (target >= nums[middle] and target <= nums[right]):
                    left = middle+1
                else:
                    right = middle - 1

        return -1