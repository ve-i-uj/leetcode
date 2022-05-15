"""53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/
"""

import sys
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.maxSubArray(*args, **kwargs)

    def maxSubArray(self, nums: List[int]) -> int:
        return sys.maxsize
