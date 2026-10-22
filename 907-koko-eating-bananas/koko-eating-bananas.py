class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_banana = max(piles)

        low = 1
        high = max_banana
        res = max_banana

        def isValid(speed):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)
            return total_time <= h

        while low <= high:
            mid = (low+high)//2
            if isValid(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1

        return res