class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                st, ht = stack.pop()
                start = st
                area = ht*(i-st)
                max_area = max(max_area, area)

            stack.append((start, h))

        
        for it, ht in stack:
            area = ht*(n-it)
            max_area = max(area, max_area)

        return max_area