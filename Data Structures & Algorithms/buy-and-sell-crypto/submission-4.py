class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxProfit, buy = 0, prices[0]
        for price in prices:
            profit = price - buy
            maxProfit = max(maxProfit, profit)
            buy = min(buy, price)
        return maxProfit

