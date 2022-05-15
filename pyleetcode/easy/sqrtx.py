"""69. Sqrtx

https://leetcode.com/problems/sqrtx/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.mySqrt(*args, **kwargs)

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        while left <= right:
            middle = left + (right - left) // 2
            prediction = middle * middle
            if x == prediction:
                return middle

            if x < prediction:
                right = middle - 1
            else:
                res = middle
                left = middle + 1

        return res
