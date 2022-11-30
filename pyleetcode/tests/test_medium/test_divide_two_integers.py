"""Unit tests of "29. Divide Two Integers".

https://leetcode.com/problems/divide-two-integers/
"""

import pytest

from pyleetcode.medium.divide_two_integers import Solution


TEST_CASES = [
    (10, 3, 3),
    (7, -3, -2),
    (-2147483648, -1, 2147483647),
]


@pytest.mark.parametrize('dividend, divisor, output', TEST_CASES)
def test(dividend: int, divisor: int, output: int):
    res = Solution().process(dividend, divisor)
    assert res == output
