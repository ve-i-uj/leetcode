"""121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        profit = 0
        for p in prices:
            profit = max(profit, p - min_price)
            min_price = min(min_price, p)

        return profit

    def process(self, *args, **kwargs):  # noqa: N802
        return self.maxProfit(*args, **kwargs)
