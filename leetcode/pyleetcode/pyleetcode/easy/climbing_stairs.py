"""70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.climbStairs(*args, **kwargs)

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        first, second = 1, 2
        for _ in range(2, n):
            first, second = second, first + second

        return second
