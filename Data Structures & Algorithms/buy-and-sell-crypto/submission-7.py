class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0

        maxprofit = 0

        profit = 0

        for sell in range(1, len(prices)):

            if prices[sell] > prices[left]:

                profit = prices[sell] - prices[left]

                if profit > maxprofit:
                    maxprofit = profit

            else:
                left = sell

        return maxprofit