"""7. Reverse Integer

https://leetcode.com/problems/reverse-integer/
"""

import math

MAX: int = 2 ** 31 - 1
MIN: int = -1 * (2 ** 31)

class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.reverse(*args, **kwargs)

    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x

        sign = 1 if x >= 0 else -1
        x = abs(x)
        n = int(math.log(x, 10) + 1)
        digit = x
        res = 0
        for i in range(n - 1, -1, -1):
            digit, the_rest = divmod(digit, 10)
            res += the_rest * (10 ** i)

            if sign * res < MIN or sign * res > MAX:
                return 0

        return res * sign
