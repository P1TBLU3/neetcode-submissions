class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        bestbuy = prices[0]
        profit = 0

        for price in prices:
            if price < bestbuy:
                bestbuy = price
            else:
                dif =  price - bestbuy 
                if dif > profit:
                    profit = dif
                
        return profit
