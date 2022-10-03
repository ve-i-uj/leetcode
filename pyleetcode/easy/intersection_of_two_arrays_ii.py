"""350. Intersection of Two Arrays II

https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

import collections
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.intersect(*args, **kwargs)

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)

        intrs = cnt2 & cnt1
        return sum(([k] * v for k, v in intrs.items()), [])
