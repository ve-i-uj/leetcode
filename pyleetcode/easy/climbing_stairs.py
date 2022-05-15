"""70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/
"""

from functools import lru_cache
from typing import Optional, List, Any  # noqa: F401


@lru_cache
def _fork(n: int) -> int:
    res = 0
    if n > 0:
        res += _fork(n - 1)
    if n > 1:
        res += _fork(n - 2)
        res += 1

    return res


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.climbStairs(*args, **kwargs)

    def climbStairs(self, n: int) -> int:
        cntr = _fork(n)
        return cntr + 1
