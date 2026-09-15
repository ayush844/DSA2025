class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        n = len(piles)

        min_ans = m

        def isValid(num):
            sum = 0
            for pile in piles:
                sum+=math.ceil(pile/num)

            return sum <= h

        left = 1
        right = m

        while left <= right:
            middle = (left+right)//2
            if isValid(middle):
                min_ans = min(min_ans, middle)
                right = middle-1
            else:
                left = middle+1

        return min_ans