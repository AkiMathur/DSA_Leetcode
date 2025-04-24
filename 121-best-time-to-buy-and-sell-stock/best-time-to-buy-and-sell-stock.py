class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = float("inf")
        selling = float("-inf")
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buying:
                buying = prices[i]
                selling = float("-inf")
            if prices[i] > selling:
                selling = prices[i]
            if (selling - buying) > profit:
                profit = selling - buying
        return profit
            
