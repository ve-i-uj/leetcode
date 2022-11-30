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
        divd = str(dividend)
        sign = 1
        if divd[0] == '-':
            sign *= -1
            divd = divd[1:]
        if divisor < 0:
            sign *= -1
            divisor *= -1

        res = ''
        the_rest = 0
        head = ''
        for x in divd:
            the_rest = int(head + x)
            cntr = 0
            while the_rest - divisor >= 0:
                cntr += 1
                the_rest -= divisor

            res += str(cntr)
            head = str(the_rest)

        if sign > 0 and res == str(MIN * -1):
            res = str(MAX)

        return int(res) * sign
