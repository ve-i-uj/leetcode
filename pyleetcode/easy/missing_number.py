"""268. Missing Number

https://leetcode.com/problems/missing-number/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.missingNumber(*args, **kwargs)

    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i

        for i in range(len(nums) + 1):
            res ^= i

        return res
