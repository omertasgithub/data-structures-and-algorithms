
#121. Best Time to Buy and Sell Stock
#array, dynamic programming



def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price-min_price
        max_profit = max(max_profit, profit)
    return max_profit