class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            maxPrice = 0
            if minPrice < price:
                maxPrice = price
            else:
                minPrice = price
            currProfit = maxPrice - minPrice
            if maxProfit < currProfit:
                maxProfit = currProfit
        return maxProfit