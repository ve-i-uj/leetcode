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
        if -10 < x < 10:
            return x

        if x == MIN:
            return 0

        is_negative = x < 0
        x = abs(x)

        res = 0
        while x != 0:
            x, the_rest = divmod(x, 10)
            if not is_negative:
                if res > MAX // 10:
                    return 0
                if res == MAX // 10 and the_rest > MAX % 10:
                    return 0

            if is_negative:
                if res > abs(MIN) // 10:
                    return 0
                if res == abs(MIN) // 10 and the_rest > abs(MIN) % 10:
                    return 0
            res = res * 10 + the_rest

        return res * -1 if is_negative else res
