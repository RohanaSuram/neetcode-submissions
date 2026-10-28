class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Update cheapest price seen so far
            min_price = min(min_price, price)

            # Calculate profit if we sell today
            profit = price - min_price
            # Update best profit
            max_profit = max(max_profit, profit)

        return max_profit