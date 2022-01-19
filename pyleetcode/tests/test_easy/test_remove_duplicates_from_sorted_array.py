"""Unit tests of 26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

import pytest

from easy.remove_duplicates_from_sorted_array import Solution


TEST_CASES = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
]


@pytest.mark.parametrize('nums, k, expected_nums', TEST_CASES)
def test_1(nums, k, expected_nums):
    res = Solution().process(nums)
    assert res == k
    assert nums[:k] == expected_nums
