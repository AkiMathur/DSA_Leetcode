class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] < buying:
                buying = prices[i]
                continue
            if (prices[i] - buying) > profit:
                profit = prices[i] - buying
        return profit
            
