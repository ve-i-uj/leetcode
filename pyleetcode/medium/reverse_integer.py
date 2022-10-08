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
        n = int(math.log(x, 10))
        digit = x
        stack = []
        for i in range(n, -1, -1):
            digit, the_rest = divmod(digit, 10)
            stack.append(the_rest)

        max_n = int(math.log(MAX, 10) + 1)

        if len(stack) < max_n:
            return sign * sum(x * (10 ** i) for i, x in enumerate(reversed(stack)))
        if len(stack) > max_n:
            return 0

        # len(stack) == max_n
        digit = MIN * -1
        max_number_stack = []
        for i in range(max_n - 1, -1, -1):
            digit, the_rest = divmod(digit, 10)
            max_number_stack.append(the_rest)

        for i, max_i in zip(stack, reversed(max_number_stack)):
            if i > max_i:
                return 0
            elif i < max_i:
                return sign * sum(x * (10 ** i) for i, x in enumerate(reversed(stack)))

        # x == MIN * -1, check the sign
        if sign > 0:
            # The value is outside
            return 0

        return sign * sum(x * (10 ** i) for i, x in enumerate(reversed(stack)))
