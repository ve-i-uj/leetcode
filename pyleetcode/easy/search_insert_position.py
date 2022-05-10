"""35. Search Insert Position

https://leetcode.com/problems/search-insert-position/
"""

import bisect
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> int:  # noqa: N802
        return self.searchInsert(*args, **kwargs)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
