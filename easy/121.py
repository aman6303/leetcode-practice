class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = min(prices)
        min_price_index = prices.index(min_price)

        new_prices = prices[min_price_index:]

        max_price = max(new_prices)

        if max_price >= min_price:
            return max_price - min_price
        else:
            return 0


# not solved yet
