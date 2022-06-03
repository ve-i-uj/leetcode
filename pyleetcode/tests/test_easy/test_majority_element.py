"""Unit tests of "169. Majority Element".

https://leetcode.com/problems/majority-element/
"""

import pytest

from easy.majority_element import Solution


TEST_CASES = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
]  # noqa


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: int):
    res = Solution().process(nums)
    assert res == output
