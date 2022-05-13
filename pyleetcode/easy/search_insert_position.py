"""35. Search Insert Position

https://leetcode.com/problems/search-insert-position/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> int:  # noqa: N802
        return self.searchInsert(*args, **kwargs)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left = -1
        right = len(nums)
        while left < right - 1:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                left = middle
            else:
                right = middle
        return right
