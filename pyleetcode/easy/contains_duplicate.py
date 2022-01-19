"""217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/
"""

from typing import Optional, List, Set, Any  # noqa: F401


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        existed: Set[int] = set()
        for el in nums:
            if el not in existed:
                existed.add(el)
            else:
                break
        else:
            return False
        return True

    def process(self, *args, **kwargs) -> bool:  # noqa: N802
        return self.containsDuplicate(*args, **kwargs)
