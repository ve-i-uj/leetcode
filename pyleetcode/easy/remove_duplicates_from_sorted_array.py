"""26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:  # noqa: N802
        ind = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[ind-1]:
                nums[ind] = nums[i]
                ind += 1

        return ind

    def process(self, *args, **kwargs):
        return self.removeDuplicates(*args, **kwargs)
