class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        maxProfit = 0
        #loop through the list starting at 1 for right
        for right in range(1, len(prices)):
            #make sure. we can subtract
            if prices[right] > prices[left]:
                #calculate profit
                profit = prices[right] - prices[left]
                #update max profit if greater
                if profit > maxProfit:
                    maxProfit = profit
            #make left the right position
            else:
                left = right

        return maxProfit