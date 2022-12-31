"""Unit tests of "33. Search in Rotated Sorted Array".

https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

import pytest

from pyleetcode.medium.search_in_rotated_sorted_array import Solution


TEST_CASES = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1, 3], 1, 0),
    ([3, 1], 3, 0),
    ([3, 5, 1], 3, 0),
]


@pytest.mark.parametrize('nums, target, output', TEST_CASES)
def test(nums: list[int], target: int, output: int):
    res = Solution().process(nums, target)
    assert res == output
