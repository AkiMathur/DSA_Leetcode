class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = prices[0]
        profit = 0
        net_profit = 0 

        for i in range(1,len(prices)):
            if prices[i] < cp:
                cp = prices[i]
            if (prices[i] - cp) > profit:
                profit = prices[i] - cp
                net_profit += profit
                cp = prices[i]
                profit = 0
        return net_profit