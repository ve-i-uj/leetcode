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

        r1 = 0
        r2 = 0
        for _ in range(m + n):
            if r2 == n:
                break
            if nums2[r2] > nums1[r1]:
                r1 += 1
                continue
            nums1.insert(r1, nums2[r2])
            r1 += 1
            r2 += 1
        if r2 < n:
            nums1[m+r2:] = nums2[r2:]

        nums1[n + m:] = []
