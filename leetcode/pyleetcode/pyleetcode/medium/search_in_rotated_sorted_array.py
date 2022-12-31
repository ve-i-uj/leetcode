"""33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

import bisect
from typing import List


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.search(*args, **kwargs)

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        first = max_x = nums[0]
        pivot_i = 0
        for i, x in enumerate(nums):
            if x < max_x:
                nums[:] = nums[i:] + nums[:i]
                pivot_i = i
                break

        index = bisect.bisect(nums, target)
        if nums[index - 1] != target:
            return -1

        res = (index - 1) + pivot_i
        if res >= len(nums):
            res -= len(nums)

        return res
