class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        res = [0]*n
        for m in reversed(range(n)):
            if nums[i]**2 > nums[j]**2:
                res[m] = nums[i]**2
                i+=1
            else:
                res[m] = nums[j]**2
                j-=1

        return res