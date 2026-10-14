class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_area = 0
        left = 0
        right = n-1

        while left < right:
            ht = min(height[left], height[right])
            wd = right-left
            area = ht*wd
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1


        return max_area