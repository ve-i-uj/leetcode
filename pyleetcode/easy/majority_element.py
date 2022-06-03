"""169. Majority Element

https://leetcode.com/problems/majority-element/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        cntr = 1
        for n in nums[1:]:
            if cntr == 0:
                num = n
                cntr = 1
                continue
            if n == num:
                cntr += 1
            else:
                cntr -= 1
        return num

    def process(self, *args, **kwargs):  # noqa: N802
        return self.majorityElement(*args, **kwargs)
