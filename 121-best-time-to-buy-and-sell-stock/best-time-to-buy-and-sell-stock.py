class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        least_price = prices[0]

        for price in prices:
            least_price = min(least_price, price)
            profit = price - least_price

            max_profit = max(max_profit, profit)

        return max_profit