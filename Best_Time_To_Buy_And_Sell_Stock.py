class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        """
        Sliding Windows two types: Dynamic and fix size
        Two pointers can also works for sliding window e.g As in this example

        """
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit
        """
        min_val = min(prices)
        if prices.index(min_val) == len(prices) - 1:
            return 0
        day_to_buy = prices.index(min_val)
        max_val = 0
        for i in range(day_to_buy + 1, len(prices)):
            max_val = max(max_val, prices[i])
        profit = max_val - min_val
        return profit
        """