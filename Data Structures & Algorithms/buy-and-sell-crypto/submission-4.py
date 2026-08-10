class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_price = 999

        for i, price in enumerate(prices):
            if price <= curr_price:
                curr_price = price
            else:
                profit = max(profit, price - curr_price)
        return profit