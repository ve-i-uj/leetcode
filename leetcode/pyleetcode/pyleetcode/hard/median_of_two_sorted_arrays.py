"""4. Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(nums1: List[int], nums2: List[int]) -> list[int]:
            short, long = sorted([nums1, nums2])

            if len(short) == 1 and len(long) == 1:
                return list(sorted([short[0], long[0]]))

            if len(short) == 1:
                val1 = short[0]
                if val1 >= long[-1]:
                    return long + [val1]
                elif val1 <= long[0]:
                    return [val1] + long
                else:
                    return [long[0]] + merge(short, long[1:])

            if short[0] <= long[0]:
                return [short[0]] + merge(short[1:], long)
            else:
                return [long[0]] + merge(short, long[1:])

        if not nums1:
            nums = nums2
        elif not nums2:
            nums = nums1
        else:
            nums = merge(nums1, nums2)
        lenght = len(nums)
        if lenght % 2 == 0:
            res = (nums[lenght // 2 - 1] + nums[lenght // 2]) / 2
        else:
            res = nums[lenght // 2]

        return res
