class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        cnt_arr = 1
        arr_pos = points[0][1]
        n = len(points)

        for i in range(1, n):
            if points[i][0] > arr_pos:
                cnt_arr += 1
                arr_pos = points[i][1]

        return cnt_arr