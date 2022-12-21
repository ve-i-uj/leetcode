"""29. Divide Two Integers

https://leetcode.com/problems/divide-two-integers/
"""

from typing import Optional, List, Any  # noqa: F401

MIN = -2147483648
MAX = 2147483647


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.divide(*args, **kwargs)

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == MIN and divisor == -1:
            return MAX
        if dividend == 0:
            return 0

        sign = 1
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        x = divisor
        while dividend >= divisor:
            y = 1
            while x <= dividend >> 1:
                x <<= 1
                y <<= 1
            dividend -= x
            res += y
            x = divisor

        return res * sign
