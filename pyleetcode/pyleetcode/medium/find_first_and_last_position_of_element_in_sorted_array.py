"""34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

import bisect
from typing import List

NO_TARGET = [-1, -1]

class Solution:

    def process(self, *args, **kwargs):
        return self.searchRange(*args, **kwargs)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        if i == len(nums) or nums[i] != target:
            return NO_TARGET
        j = i
        for j, n in enumerate(nums[i:], start=i):
            if n != target:
                j -= 1
                break

        return [i, j]
