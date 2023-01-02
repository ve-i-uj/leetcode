"""Unit tests of "4. Median of Two Sorted Arrays".

https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

import pytest

from pyleetcode.hard.median_of_two_sorted_arrays import Solution


TEST_CASES = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([1], [], 1),
    ([], [1], 1),
    ([0,0,0,0,0], [-1,0,0,0,0,0,1], 0),
]

@pytest.mark.parametrize('nums1, nums2, output', TEST_CASES)
def test(nums1: list[int], nums2: list[int], output: float):
    res = Solution().findMedianSortedArrays(nums1, nums2)
    assert res == output
