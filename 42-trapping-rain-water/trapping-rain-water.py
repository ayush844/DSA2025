class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n-1

        leftMax, rightMax = height[l], height[r]

        res = 0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res+=(leftMax-height[l])
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res+=(rightMax-height[r])

        return res