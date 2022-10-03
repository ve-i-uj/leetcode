"""326. Power of Three

https://leetcode.com/problems/power-of-three/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isPowerOfThree(*args, **kwargs)

    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        while n % 3 == 0:
            n //= 3

        return n == 1
