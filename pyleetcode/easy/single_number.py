"""136. Single Number

https://leetcode.com/problems/single-number/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result

    def process(self, *args, **kwargs):  # noqa: N802
        return self.singleNumber(*args, **kwargs)
