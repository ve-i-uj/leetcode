"""Unit tests of "268. Missing Number".

https://leetcode.com/problems/missing-number/
"""

import pytest

from pyleetcode.easy.missing_number import Solution


TEST_CASES = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
]  # noqa


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: int):
    res = Solution().process(nums)
    assert output == res

