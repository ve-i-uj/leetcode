"""Unit tests of "121. Best Time to Buy and Sell Stock".

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

import pytest

from easy.best_time_to_buy_and_sell_stock import Solution


TEST_CASES = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
]


@pytest.mark.parametrize('prices, profit', TEST_CASES)
def test(prices: list[int], profit: int):
    res = Solution().process(prices)
    assert res == profit
