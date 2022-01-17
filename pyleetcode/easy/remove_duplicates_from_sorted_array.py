"""26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import Optional, List, Any


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if len(nums) == 1:
            return 1

        # We have two values in the list at this point.
        stop_pos = length
        last = nums[0]
        cur_pos = 1
        while cur_pos < stop_pos:
            if nums[cur_pos] == last:
                # move a duplicate element to the end of the list
                nums.append(nums.pop(cur_pos))
                stop_pos -= 1
            else:
                last = nums[cur_pos]
                cur_pos += 1

        return stop_pos

    def process(self, *args, **kwargs):
        return self.removeDuplicates(*args, **kwargs)
