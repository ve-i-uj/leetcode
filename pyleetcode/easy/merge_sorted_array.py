"""88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.merge(*args, **kwargs)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int
              ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]
            return

        r1 = m - 1
        r2 = n - 1
        for i in reversed(range(n + m)):
            if r2 < 0 or r1 < 0:
                break
            if nums1[r1] > nums2[r2]:
                nums1[i] = nums1[r1]
                nums1[r1] = 0
                r1 -= 1
            else:
                nums1[i] = nums2[r2]
                r2 -= 1

        if r2 >= 0:
            nums1[:i+1] = nums2[:r2+1]
