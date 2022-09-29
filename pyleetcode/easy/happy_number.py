"""202. Happy Number

https://leetcode.com/problems/happy-number/
"""

import sys
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isHappy(*args, **kwargs)

    def isHappy(self, n: int) -> bool:
        nums = set()
        nums.add(n)
        for _ in range(sys.maxsize):
            n = sum(int(i) ** 2 for i in str(n))
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)
        return False
