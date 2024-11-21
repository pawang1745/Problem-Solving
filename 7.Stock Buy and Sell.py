from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
