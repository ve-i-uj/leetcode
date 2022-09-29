"""191. Number of 1 Bits

https://leetcode.com/problems/number-of-bits/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.hammingWeight(*args, **kwargs)

    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        return s.count('1')
