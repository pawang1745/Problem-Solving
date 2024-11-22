class Solution:
    def maximumProfit(self, prices):
        # code here
        if len(prices) < 2:
            return 0
            
        minprice = float('inf')
        maxprofit = 0
        
        for i in prices:
            minprice = min(i, minprice)
            
            cp = i - minprice
            
            maxprofit = max(cp, maxprofit)
        return maxprofit
