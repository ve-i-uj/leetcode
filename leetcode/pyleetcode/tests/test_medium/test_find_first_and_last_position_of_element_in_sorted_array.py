"""Unit tests of "34. Find First and Last Position of Element in Sorted Array".

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

import pytest

from pyleetcode.medium.find_first_and_last_position_of_element_in_sorted_array import Solution


TEST_CASES = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
]


@pytest.mark.parametrize('nums, target, output', TEST_CASES)
def test(nums: list[int], target: int, output: list[int]):
    res = Solution().process(nums, target)
    assert res == output
