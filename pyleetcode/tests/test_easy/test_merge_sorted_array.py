"""Unit tests of "88. Merge Sorted Array".

https://leetcode.com/problems/merge-sorted-array/
"""

import pytest

from easy.merge_sorted_array import Solution


TEST_CASES = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([2, 0], 1, [1], 1, [1, 2]),
    ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
    ([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5, [1, 2, 3, 4, 5, 6]),
]


@pytest.mark.parametrize('nums1, m, nums2, n, output', TEST_CASES)
def test(nums1: list[int], m: int, nums2: list[int], n: int, output: list[int]):
    Solution().process(nums1, m, nums2, n)
    assert nums1 == output
