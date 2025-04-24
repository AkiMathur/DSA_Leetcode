class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = float("inf")
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buying:
                buying = prices[i]
            if (prices[i] - buying) > profit:
                profit = prices[i] - buying
        return profit
            
