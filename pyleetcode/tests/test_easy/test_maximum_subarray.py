"""Unit tests of "53. Maximum Subarray".

https://leetcode.com/problems/maximum-subarray/
"""

import pytest

from easy.maximum_subarray import Solution


TEST_CASES = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
]  # noqa


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: int):
    res = Solution().process(nums)
    assert res == output
