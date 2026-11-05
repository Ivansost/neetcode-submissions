class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        maxprofit = 0
    
        for sell in range(len(prices)):

            profit = prices[sell] - prices[buy]

            if profit > maxprofit:
                maxprofit = profit

            if prices[sell] < prices[buy]:
                buy = sell

        return maxprofit        

