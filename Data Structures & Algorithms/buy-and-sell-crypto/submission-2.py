class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            currentProfit = price - minPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit
            
        return maxProfit