"""53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/
"""

import sys
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.maxSubArray(*args, **kwargs)

    def maxSubArray(self, nums: List[int]) -> int:
        local_maximum = 0
        global_maximum = ~sys.maxsize

        for x in nums:
            local_maximum = max(x, x + local_maximum)
            if local_maximum > global_maximum:
                global_maximum = local_maximum
        return global_maximum
