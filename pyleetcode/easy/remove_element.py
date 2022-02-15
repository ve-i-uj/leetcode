"""27. Remove Element

https://leetcode.com/problems/remove-element/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> int:  # noqa: N802
        return self.removeElement(*args, **kwargs)

    def removeElement(self, nums: List[int], val: int) -> int:   # noqa: N802
        r_i = 0
        w_i = 0
        n_len = len(nums)
        while r_i < n_len:
            el = nums[r_i]
            if el == val:
                r_i += 1
                continue
            nums[w_i] = nums[r_i]
            w_i += 1
            r_i += 1

        return w_i
