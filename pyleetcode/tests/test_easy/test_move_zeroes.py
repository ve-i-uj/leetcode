"""Unit tests of "283. Move Zeroes".

https://leetcode.com/problems/move-zeroes/
"""

import pytest

from easy.move_zeroes import Solution


TEST_CASES = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1], [1]),
]  # noqa


@pytest.mark.parametrize('nums, res', TEST_CASES)
def test(nums: list, res: list):
    Solution().process(nums)
    assert nums == res
