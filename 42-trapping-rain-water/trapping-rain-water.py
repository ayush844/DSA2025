class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        res = 0

        left_max, right_max = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l+=1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res