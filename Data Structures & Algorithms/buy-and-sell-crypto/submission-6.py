class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        left = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[left]:
                profit = prices[i] - prices[left]

                if profit > maxp:
                    maxp = profit

            else:
                left = i

        return maxp