"""283. Move Zeroes

https://leetcode.com/problems/move-zeroes/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.moveZeroes(*args, **kwargs)

    def moveZeroes(self, nums: List[int]) -> None:
        w_pos = 0
        for r_pos in range(len(nums)):
            if nums[r_pos] == 0:
                r_pos += 1
                continue
            val = nums[r_pos]
            nums[r_pos] = 0
            nums[w_pos] = val
            r_pos += 1
            w_pos += 1
