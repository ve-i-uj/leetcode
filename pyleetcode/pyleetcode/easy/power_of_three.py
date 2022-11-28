"""326. Power of Three

https://leetcode.com/problems/power-of-three/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isPowerOfThree(*args, **kwargs)

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
